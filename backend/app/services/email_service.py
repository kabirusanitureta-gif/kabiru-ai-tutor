"""
Outgoing email for Kabiru AI Tutor: password-reset codes, email verification,
and account security alerts.

Uses only the Python standard library (smtplib/email) so no new dependency
is required. If SMTP_* settings aren't configured (settings.email_configured
is False), every message is logged instead of sent — this keeps local/dev/
offline setups working exactly as before, and never crashes a request just
because email isn't set up yet in this environment.
"""
import logging
import smtplib
from email.message import EmailMessage

from app.core.config import settings

logger = logging.getLogger("kabiru.email")


def _send(to_email: str, subject: str, body: str, *, log_label: str) -> None:
    """Shared send path for every email in this module. Never raises —
    a failed or unconfigured send is logged and swallowed so it can never
    block the auth/security flow that triggered it (login, password reset,
    passkey registration, etc.)."""
    if not settings.email_configured:
        logger.info(
            "SMTP not configured — %s for %s not sent (configure "
            "SMTP_HOST/SMTP_USER/SMTP_PASSWORD to send real emails). Subject: %s",
            log_label,
            to_email,
            subject,
        )
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_email
    msg.set_content(body)

    try:
        if settings.SMTP_USE_TLS:
            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
                server.starttls()
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.send_message(msg)
        else:
            with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.send_message(msg)
    except Exception:
        # Never let an SMTP outage break the request, and never log the
        # message body (it may contain a reset code/PIN) — only that the
        # send failed and to whom, which is enough for ops to notice.
        logger.exception("Failed to send %s to %s", log_label, to_email)


def send_password_reset_email(to_email: str, full_name: str, reset_code: str) -> None:
    subject = "Your Kabiru AI Tutor password reset code"
    body = (
        f"Hi {full_name},\n\n"
        f"Your password reset code is: {reset_code}\n\n"
        f"This code expires in {settings.PASSWORD_RESET_TOKEN_EXPIRE_MINUTES} minutes. "
        f"If you didn't request this, you can safely ignore this email.\n\n"
        f"— {settings.APP_NAME}"
    )
    _send(to_email, subject, body, log_label="password reset code")


def send_verification_email(to_email: str, full_name: str, pin: str) -> None:
    subject = "Verify your Kabiru AI Tutor email"
    body = (
        f"Hi {full_name},\n\n"
        f"Your email verification PIN is: {pin}\n\n"
        f"Enter this code in the app to activate your account. It expires in "
        f"{settings.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES} minutes. "
        f"If you didn't create this account, you can safely ignore this email.\n\n"
        f"— {settings.APP_NAME}"
    )
    _send(to_email, subject, body, log_label="verification PIN")


# ---------------------------------------------------------------------------
# Security alert emails
# ---------------------------------------------------------------------------
# All of these are best-effort notifications: the security-relevant action
# (password reset, passkey added/removed, login) has ALREADY happened by the
# time these are called. A failed alert email must never undo the action or
# block the response — see the call sites in routers/auth.py and
# routers/webauthn.py, which call these after commit() and ignore failures.

def send_password_changed_alert(to_email: str, full_name: str, when: str) -> None:
    subject = f"Your {settings.APP_NAME} password was changed"
    body = (
        f"Hi {full_name},\n\n"
        f"Your {settings.APP_NAME} password was changed on {when}.\n\n"
        f"All of your other devices have been signed out as a precaution — "
        f"you'll need to log in again on them with your new password.\n\n"
        f"If you didn't make this change, please reset your password again "
        f"immediately using \"Forgot password\" on the login screen.\n\n"
        f"— {settings.APP_NAME}"
    )
    _send(to_email, subject, body, log_label="password-changed alert")


def send_new_device_login_alert(to_email: str, full_name: str, when: str, device_info: str) -> None:
    subject = f"New sign-in to your {settings.APP_NAME} account"
    body = (
        f"Hi {full_name},\n\n"
        f"Your account was just signed in from a device we haven't seen before:\n\n"
        f"  Time: {when}\n"
        f"  Device: {device_info}\n\n"
        f"If this was you, no action is needed. If it wasn't, reset your "
        f"password immediately using \"Forgot password\" on the login screen.\n\n"
        f"— {settings.APP_NAME}"
    )
    _send(to_email, subject, body, log_label="new-device login alert")


def send_webauthn_added_alert(to_email: str, full_name: str, device_name: str, when: str) -> None:
    subject = f"Face ID / passkey added to your {settings.APP_NAME} account"
    body = (
        f"Hi {full_name},\n\n"
        f"A new Face ID / Touch ID / passkey (\"{device_name}\") was added to your "
        f"account on {when}. It can now be used to sign in without your password.\n\n"
        f"If you didn't do this, remove it immediately from Settings → Face ID / "
        f"Biometric Login, and change your password.\n\n"
        f"— {settings.APP_NAME}"
    )
    _send(to_email, subject, body, log_label="passkey-added alert")


def send_webauthn_removed_alert(to_email: str, full_name: str, device_name: str, when: str) -> None:
    subject = f"Face ID / passkey removed from your {settings.APP_NAME} account"
    body = (
        f"Hi {full_name},\n\n"
        f"The passkey \"{device_name}\" was removed from your account on {when}. "
        f"It can no longer be used to sign in.\n\n"
        f"If you didn't do this, please change your password immediately.\n\n"
        f"— {settings.APP_NAME}"
    )
    _send(to_email, subject, body, log_label="passkey-removed alert")
