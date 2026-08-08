"""
WebAuthn (Face ID / Touch ID / Windows Hello / security keys) endpoints.

This is standard passwordless/biometric login via the browser's WebAuthn
API (the same mechanism behind "Sign in with passkey" on most major
sites). Nothing biometric ever reaches this server or is ever sent over
the network: the user's device performs the Face ID / Touch ID / PIN check
locally, then uses a private key that never leaves that device to sign a
challenge. This backend only ever stores the corresponding *public* key —
mathematically useless for impersonating the user without the private half.

Flow:
  1. Registration (must already be logged in with a password once):
       POST /register/options  -> browser prompts "set up Face ID"
       POST /register/verify   -> stores the new public key
  2. Login (no prior session needed):
       POST /login/options     -> browser prompts Face ID / Touch ID
       POST /login/verify      -> issues the normal JWT access/refresh pair,
                                   exactly like /api/auth/login-json does
  3. Managing enrolled passkeys: GET/PATCH/DELETE /credentials
"""
import json
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from webauthn import (
    generate_authentication_options,
    generate_registration_options,
    options_to_json,
    verify_authentication_response,
    verify_registration_response,
)
from webauthn.helpers import base64url_to_bytes, bytes_to_base64url
from webauthn.helpers.structs import (
    AuthenticatorAttachment,
    AuthenticatorSelectionCriteria,
    PublicKeyCredentialDescriptor,
    ResidentKeyRequirement,
    UserVerificationRequirement,
)

from app.core.audit import log_action
from app.core.config import settings
from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.rate_limit import check_rate_limit, clear_attempts, record_attempt
from app.core.security import create_access_token
from app.core.webauthn_store import pop_challenge, save_challenge
from app.models.models import User, WebAuthnCredential
from app.routers.auth import _issue_refresh_token
from app.services.email_service import send_webauthn_added_alert, send_webauthn_removed_alert
from app.schemas.auth import (
    Token,
    UserOut,
    WebAuthnCredentialOut,
    WebAuthnCredentialRename,
    WebAuthnLoginOptionsRequest,
    WebAuthnLoginVerifyRequest,
    WebAuthnRegisterVerifyRequest,
)

router = APIRouter(prefix="/api/auth/webauthn", tags=["webauthn"])


def _parse_transports(transports: str | None) -> list[str] | None:
    return transports.split(",") if transports else None


def _guess_device_name(request: Request) -> str:
    """Best-effort human-friendly default label from the User-Agent, used
    only when the client didn't supply its own device_name."""
    ua = (request.headers.get("user-agent") or "").lower()
    if "iphone" in ua:
        return "iPhone (Face ID / Touch ID)"
    if "ipad" in ua:
        return "iPad (Face ID / Touch ID)"
    if "mac" in ua:
        return "Mac (Touch ID)"
    if "android" in ua:
        return "Android device"
    if "windows" in ua:
        return "Windows device (Windows Hello)"
    return "Passkey"


def _verify_against_allowed_origins(verify_fn, **kwargs):
    """py_webauthn's expected_origin parameter isn't consistently a
    single-vs-list API across versions, so try every configured origin in
    turn rather than depending on that. Succeeds on the first origin that
    validates; re-raises the last error if none do."""
    last_exc = None
    for origin in settings.webauthn_origins_list:
        try:
            return verify_fn(expected_origin=origin, **kwargs)
        except Exception as exc:  # noqa: BLE001 - deliberately broad, see docstring
            last_exc = exc
    raise last_exc


# ---------------------------------------------------------------------------
# Registration (adding a new passkey to an already-authenticated account)
# ---------------------------------------------------------------------------

@router.post("/register/options")
def webauthn_register_options(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    existing = db.query(WebAuthnCredential).filter(WebAuthnCredential.user_id == current_user.id).all()
    exclude_credentials = [
        PublicKeyCredentialDescriptor(
            id=base64url_to_bytes(c.credential_id),
            transports=_parse_transports(c.transports),
        )
        for c in existing
    ]

    options = generate_registration_options(
        rp_id=settings.WEBAUTHN_RP_ID,
        rp_name=settings.WEBAUTHN_RP_NAME,
        user_id=str(current_user.id).encode("utf-8"),
        user_name=current_user.email,
        user_display_name=current_user.full_name,
        authenticator_selection=AuthenticatorSelectionCriteria(
            # PLATFORM restricts this to the device's own built-in
            # authenticator (Face ID / Touch ID / Windows Hello) rather than
            # a roaming USB security key, matching what was asked for.
            authenticator_attachment=AuthenticatorAttachment.PLATFORM,
            resident_key=ResidentKeyRequirement.PREFERRED,
            user_verification=UserVerificationRequirement.REQUIRED,
        ),
        exclude_credentials=exclude_credentials or None,
    )
    state_id = save_challenge(options.challenge, user_id=current_user.id)
    return {"state_id": state_id, "options": json.loads(options_to_json(options))}


@router.post("/register/verify", response_model=WebAuthnCredentialOut, status_code=status.HTTP_201_CREATED)
def webauthn_register_verify(
    payload: WebAuthnRegisterVerifyRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    state = pop_challenge(payload.state_id)
    if not state or state.get("user_id") != current_user.id:
        raise HTTPException(status_code=400, detail="Registration session expired. Please try again.")

    try:
        verified = _verify_against_allowed_origins(
            verify_registration_response,
            credential=json.dumps(payload.credential),
            expected_challenge=state["challenge"],
            expected_rp_id=settings.WEBAUTHN_RP_ID,
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Could not verify that passkey. Please try again.")

    credential_id_b64 = bytes_to_base64url(verified.credential_id)
    if db.query(WebAuthnCredential).filter(WebAuthnCredential.credential_id == credential_id_b64).first():
        raise HTTPException(status_code=400, detail="This passkey is already registered.")

    transports = (payload.credential.get("response") or {}).get("transports") or []
    device_name = (payload.device_name or "").strip()[:120] or _guess_device_name(request)

    row = WebAuthnCredential(
        user_id=current_user.id,
        credential_id=credential_id_b64,
        public_key=bytes_to_base64url(verified.credential_public_key),
        sign_count=verified.sign_count,
        transports=",".join(transports) if transports else None,
        device_name=device_name,
    )
    db.add(row)
    db.commit()
    db.refresh(row)

    log_action(
        db, "webauthn_credential_registered", actor=current_user,
        entity_type="webauthn_credential", entity_id=row.id, details=device_name, request=request,
    )
    try:
        send_webauthn_added_alert(
            current_user.email, current_user.full_name, device_name,
            datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        )
    except Exception:
        # Best-effort only — the passkey is already saved and committed;
        # a failed alert email must not undo or fail the registration.
        logging.getLogger("kabiru.email").exception(
            "Passkey-added alert failed for user %s", current_user.id
        )
    return row


# ---------------------------------------------------------------------------
# Login (no prior session required)
# ---------------------------------------------------------------------------

@router.post("/login/options")
def webauthn_login_options(payload: WebAuthnLoginOptionsRequest, db: Session = Depends(get_db)):
    allow_credentials = None
    email = None
    if payload.email:
        email = payload.email.lower().strip()
        user = db.query(User).filter(User.email == email).first()
        if user:
            creds = db.query(WebAuthnCredential).filter(WebAuthnCredential.user_id == user.id).all()
            allow_credentials = [
                PublicKeyCredentialDescriptor(
                    id=base64url_to_bytes(c.credential_id),
                    transports=_parse_transports(c.transports),
                )
                for c in creds
            ] or None
        # If the user or their credentials aren't found, allow_credentials
        # simply stays None and the options below are still valid — this
        # endpoint never reveals whether an email is registered.

    options = generate_authentication_options(
        rp_id=settings.WEBAUTHN_RP_ID,
        allow_credentials=allow_credentials,
        user_verification=UserVerificationRequirement.REQUIRED,
    )
    state_id = save_challenge(options.challenge, email=email)
    return {"state_id": state_id, "options": json.loads(options_to_json(options))}


@router.post("/login/verify", response_model=Token)
def webauthn_login_verify(payload: WebAuthnLoginVerifyRequest, request: Request, db: Session = Depends(get_db)):
    state = pop_challenge(payload.state_id)
    if not state:
        raise HTTPException(status_code=400, detail="Login session expired. Please try again.")

    credential_id_b64 = payload.credential.get("id") or payload.credential.get("rawId")
    if not credential_id_b64:
        raise HTTPException(status_code=400, detail="Malformed passkey response.")

    check_rate_limit(request, credential_id_b64, scope="webauthn-login")

    stored = db.query(WebAuthnCredential).filter(WebAuthnCredential.credential_id == credential_id_b64).first()
    if not stored:
        record_attempt(request, credential_id_b64, scope="webauthn-login")
        raise HTTPException(status_code=401, detail="Passkey not recognized.")

    user = db.query(User).filter(User.id == stored.user_id).first()
    if not user or not user.is_active or user.is_deleted:
        record_attempt(request, credential_id_b64, scope="webauthn-login")
        raise HTTPException(status_code=403, detail="Account is disabled")

    try:
        verified = _verify_against_allowed_origins(
            verify_authentication_response,
            credential=json.dumps(payload.credential),
            expected_challenge=state["challenge"],
            expected_rp_id=settings.WEBAUTHN_RP_ID,
            credential_public_key=base64url_to_bytes(stored.public_key),
            credential_current_sign_count=stored.sign_count,
        )
    except Exception:
        record_attempt(request, credential_id_b64, scope="webauthn-login")
        log_action(db, "webauthn_login_failed", entity_type="user", entity_id=user.id, request=request)
        raise HTTPException(status_code=401, detail="Passkey verification failed.")

    clear_attempts(request, credential_id_b64, scope="webauthn-login")
    stored.sign_count = verified.new_sign_count
    stored.last_used_at = datetime.utcnow()
    db.commit()

    token = create_access_token({"sub": str(user.id)})
    refresh_token = _issue_refresh_token(db, user, request)
    log_action(db, "webauthn_login_success", actor=user, entity_type="user", entity_id=user.id, request=request)
    return Token(access_token=token, user=UserOut.model_validate(user), refresh_token=refresh_token)


# ---------------------------------------------------------------------------
# Managing enrolled passkeys
# ---------------------------------------------------------------------------

@router.get("/credentials", response_model=list[WebAuthnCredentialOut])
def list_my_credentials(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return (
        db.query(WebAuthnCredential)
        .filter(WebAuthnCredential.user_id == current_user.id)
        .order_by(WebAuthnCredential.created_at.desc())
        .all()
    )


@router.patch("/credentials/{credential_id}", response_model=WebAuthnCredentialOut)
def rename_my_credential(
    credential_id: int,
    payload: WebAuthnCredentialRename,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    row = (
        db.query(WebAuthnCredential)
        .filter(WebAuthnCredential.id == credential_id, WebAuthnCredential.user_id == current_user.id)
        .first()
    )
    if not row:
        raise HTTPException(status_code=404, detail="Passkey not found.")
    row.device_name = payload.device_name.strip()
    db.commit()
    db.refresh(row)
    return row


@router.delete("/credentials/{credential_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_credential(
    credential_id: int,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    row = (
        db.query(WebAuthnCredential)
        .filter(WebAuthnCredential.id == credential_id, WebAuthnCredential.user_id == current_user.id)
        .first()
    )
    if not row:
        raise HTTPException(status_code=404, detail="Passkey not found.")
    device_name = row.device_name or "Passkey"
    db.delete(row)
    db.commit()
    log_action(
        db, "webauthn_credential_removed", actor=current_user,
        entity_type="webauthn_credential", entity_id=credential_id, request=request,
    )
    try:
        send_webauthn_removed_alert(
            current_user.email, current_user.full_name, device_name,
            datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        )
    except Exception:
        logging.getLogger("kabiru.email").exception(
            "Passkey-removed alert failed for user %s", current_user.id
        )
    return None
