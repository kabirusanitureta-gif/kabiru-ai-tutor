import os
import uuid
from datetime import date, datetime, timedelta

from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.audit import log_action
from app.core.config import settings
from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.rate_limit import check_rate_limit, clear_attempts, record_attempt
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    generate_refresh_token,
    generate_reset_code,
    hash_token,
)
from app.models.models import User, StudyStreak, RefreshToken, PasswordResetToken
from app.schemas.auth import (
    UserCreate,
    UserLogin,
    UserOut,
    Token,
    UserUpdate,
    RefreshTokenRequest,
    LogoutRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
)
from app.services.email_service import send_password_reset_email

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _issue_refresh_token(db: Session, user: User, request: Request) -> str:
    """Create a new refresh token row and return the plaintext token (stored hashed)."""
    plaintext = generate_refresh_token()
    row = RefreshToken(
        user_id=user.id,
        token_hash=hash_token(plaintext),
        expires_at=datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        user_agent=(request.headers.get("user-agent", "")[:255] if request else None),
    )
    db.add(row)
    db.commit()
    return plaintext


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, request: Request, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        full_name=payload.full_name,
        email=payload.email,
        hashed_password=hash_password(payload.password),
        preferred_language=payload.preferred_language,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    streak = StudyStreak(user_id=user.id, current_streak=0, longest_streak=0, last_active_date=date.today())
    db.add(streak)
    db.commit()

    token = create_access_token({"sub": str(user.id)})
    refresh_token = _issue_refresh_token(db, user, request)
    log_action(db, "user_registered", actor=user, entity_type="user", entity_id=user.id, request=request)
    return Token(access_token=token, user=UserOut.model_validate(user), refresh_token=refresh_token)


@router.post("/login", response_model=Token)
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    check_rate_limit(request, form_data.username, scope="login")

    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        record_attempt(request, form_data.username, scope="login")
        log_action(db, "login_failed", entity_type="user", details=form_data.username, request=request)
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    if not user.is_active or user.is_deleted:
        log_action(db, "login_blocked_inactive", actor=user, entity_type="user", entity_id=user.id, request=request)
        raise HTTPException(status_code=403, detail="Account is disabled")

    clear_attempts(request, form_data.username, scope="login")
    token = create_access_token({"sub": str(user.id)})
    refresh_token = _issue_refresh_token(db, user, request)
    log_action(db, "login_success", actor=user, entity_type="user", entity_id=user.id, request=request)
    return Token(access_token=token, user=UserOut.model_validate(user), refresh_token=refresh_token)


@router.post("/login-json", response_model=Token)
def login_json(payload: UserLogin, request: Request, db: Session = Depends(get_db)):
    """Alternative JSON login endpoint (easier for the React frontend than form-encoded)."""
    check_rate_limit(request, payload.email, scope="login")

    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        record_attempt(request, payload.email, scope="login")
        log_action(db, "login_failed", entity_type="user", details=payload.email, request=request)
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    if not user.is_active or user.is_deleted:
        log_action(db, "login_blocked_inactive", actor=user, entity_type="user", entity_id=user.id, request=request)
        raise HTTPException(status_code=403, detail="Account is disabled")

    clear_attempts(request, payload.email, scope="login")
    token = create_access_token({"sub": str(user.id)})
    refresh_token = _issue_refresh_token(db, user, request)
    log_action(db, "login_success", actor=user, entity_type="user", entity_id=user.id, request=request)
    return Token(access_token=token, user=UserOut.model_validate(user), refresh_token=refresh_token)


@router.post("/refresh", response_model=Token)
def refresh_token_endpoint(payload: RefreshTokenRequest, request: Request, db: Session = Depends(get_db)):
    """Exchange a valid refresh token for a new access token. Rotates the refresh token."""
    token_hash = hash_token(payload.refresh_token)
    row = db.query(RefreshToken).filter(RefreshToken.token_hash == token_hash).first()

    invalid_exc = HTTPException(status_code=401, detail="Invalid or expired refresh token")
    if not row or row.revoked or row.expires_at < datetime.utcnow():
        raise invalid_exc

    user = db.query(User).filter(User.id == row.user_id).first()
    if not user or not user.is_active:
        raise invalid_exc

    # Rotate: revoke the used token, issue a fresh one. Limits the damage
    # window if a refresh token is ever intercepted.
    row.revoked = True
    db.commit()

    new_access = create_access_token({"sub": str(user.id)})
    new_refresh = _issue_refresh_token(db, user, request)
    return Token(access_token=new_access, user=UserOut.model_validate(user), refresh_token=new_refresh)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(payload: LogoutRequest, db: Session = Depends(get_db)):
    """Revoke a single refresh token (this device only). Access tokens simply expire on their own."""
    token_hash = hash_token(payload.refresh_token)
    row = db.query(RefreshToken).filter(RefreshToken.token_hash == token_hash).first()
    if row:
        row.revoked = True
        db.commit()
    return None


@router.post("/forgot-password", status_code=status.HTTP_202_ACCEPTED)
def forgot_password(payload: ForgotPasswordRequest, request: Request, db: Session = Depends(get_db)):
    """
    Always returns the same generic response whether or not the email exists,
    so the endpoint can't be used to check which emails are registered.
    """
    check_rate_limit(request, payload.email, scope="forgot-password")
    record_attempt(request, payload.email, scope="forgot-password")

    user = db.query(User).filter(User.email == payload.email).first()
    if user:
        code = generate_reset_code()
        reset_row = PasswordResetToken(
            user_id=user.id,
            token_hash=hash_token(code),
            expires_at=datetime.utcnow() + timedelta(minutes=settings.PASSWORD_RESET_TOKEN_EXPIRE_MINUTES),
        )
        db.add(reset_row)
        db.commit()
        send_password_reset_email(user.email, user.full_name, code)

    return {"message": "If that email is registered, a reset code has been sent."}


@router.post("/reset-password", status_code=status.HTTP_200_OK)
def reset_password(payload: ResetPasswordRequest, request: Request, db: Session = Depends(get_db)):
    check_rate_limit(request, payload.email, scope="reset-password")

    user = db.query(User).filter(User.email == payload.email).first()
    generic_error = HTTPException(status_code=400, detail="Invalid or expired reset code")
    if not user:
        record_attempt(request, payload.email, scope="reset-password")
        raise generic_error

    code_hash = hash_token(payload.code)
    reset_row = (
        db.query(PasswordResetToken)
        .filter(PasswordResetToken.user_id == user.id, PasswordResetToken.token_hash == code_hash)
        .order_by(PasswordResetToken.created_at.desc())
        .first()
    )
    if not reset_row or reset_row.used or reset_row.expires_at < datetime.utcnow():
        record_attempt(request, payload.email, scope="reset-password")
        raise generic_error

    user.hashed_password = hash_password(payload.new_password)
    reset_row.used = True
    # Force re-login everywhere: any stolen session should die the moment
    # the account owner regains control via password reset.
    db.query(RefreshToken).filter(RefreshToken.user_id == user.id, RefreshToken.revoked.is_(False)).update(
        {"revoked": True}
    )
    db.commit()
    clear_attempts(request, payload.email, scope="reset-password")
    clear_attempts(request, payload.email, scope="login")
    log_action(db, "password_reset", actor=user, entity_type="user", entity_id=user.id, request=request)

    return {"message": "Password reset successfully. Please log in with your new password."}


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/me", response_model=UserOut)
def update_me(payload: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if payload.full_name is not None:
        current_user.full_name = payload.full_name
    if payload.preferred_language is not None:
        current_user.preferred_language = payload.preferred_language
    if payload.theme is not None:
        current_user.theme = payload.theme
    db.commit()
    db.refresh(current_user)
    return current_user


_AVATAR_DIR = os.path.join(settings.UPLOAD_DIR, "avatars")
_EXT_BY_CONTENT_TYPE = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}


def _delete_avatar_file(avatar_path: str | None) -> None:
    if not avatar_path:
        return
    full_path = os.path.join(_AVATAR_DIR, avatar_path)
    # Defensive: avatar_path is always a bare filename we generated
    # ourselves (see upload_my_photo), never a path from client input, so
    # this can't be used to escape _AVATAR_DIR.
    try:
        if os.path.isfile(full_path):
            os.remove(full_path)
    except OSError:
        pass


@router.post("/me/photo", response_model=UserOut)
def upload_my_photo(
    request: Request,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Upload/replace the current user's profile photo. Accepts jpeg/png/webp
    up to AVATAR_MAX_SIZE_MB. Replaces any previous photo (old file removed)."""
    content_type = (file.content_type or "").lower()
    if content_type not in settings.avatar_allowed_content_types_list:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported image type '{content_type}'. Allowed: {settings.AVATAR_ALLOWED_CONTENT_TYPES}",
        )

    max_bytes = settings.AVATAR_MAX_SIZE_MB * 1024 * 1024
    contents = file.file.read(max_bytes + 1)
    if len(contents) > max_bytes:
        raise HTTPException(status_code=400, detail=f"Image too large. Max size is {settings.AVATAR_MAX_SIZE_MB}MB.")
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    os.makedirs(_AVATAR_DIR, exist_ok=True)
    ext = _EXT_BY_CONTENT_TYPE.get(content_type, ".jpg")
    # Random filename (never derived from the client-supplied filename) so a
    # crafted filename can't be used for path traversal or to collide with
    # another user's file.
    filename = f"{uuid.uuid4().hex}{ext}"
    full_path = os.path.join(_AVATAR_DIR, filename)
    with open(full_path, "wb") as f:
        f.write(contents)

    old_avatar = current_user.avatar_path
    current_user.avatar_path = filename
    db.commit()
    db.refresh(current_user)
    _delete_avatar_file(old_avatar)

    log_action(db, "avatar_uploaded", actor=current_user, entity_type="user", entity_id=current_user.id, request=request)
    return current_user


@router.delete("/me/photo", response_model=UserOut)
def delete_my_photo(request: Request, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    old_avatar = current_user.avatar_path
    current_user.avatar_path = None
    db.commit()
    db.refresh(current_user)
    _delete_avatar_file(old_avatar)

    log_action(db, "avatar_deleted", actor=current_user, entity_type="user", entity_id=current_user.id, request=request)
    return current_user
