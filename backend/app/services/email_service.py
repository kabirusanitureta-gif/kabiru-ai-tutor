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
import socket
from contextlib import contextmanager
from email.message import EmailMessage

from app.core.config import settings

logger = logging.getLogger("kabiru.email")


@contextmanager
def _force_ipv4_dns():
    """
    Some hosts (Render's free tier among them) have no outbound IPv6 route,
    but smtp.gmail.com resolves to both an IPv6 (AAAA) and IPv4 (A) address.
    getaddrinfo() can return the IPv6 result first, and smtplib then tries
    to connect to an address the container can't reach at all — failing
    immediately with OSError: [Errno 101] Network is unreachable, before
    SMTP/TLS/auth ever run.

    This temporarily filters getaddrinfo to IPv4-only for the duration of
    the SMTP connection. The hostname itself is still what's passed to
    smtplib and used for the STARTTLS certificate check — only the
    underlying IP resolution changes. Restored via try/finally so nothing
    else in the process is affected.
    """
    original_getaddrinfo = socket.getaddrinfo

    def ipv4_only_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        return original_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)

    socket.getaddrinfo = ipv4_only_getaddrinfo
    try:
        yield
    finally:
        socket.getaddrinfo = original_getaddrinfo


def _send(to_email: str, subject: str, body: str, *, log_label: str) -> None:
    """Shared send path for every email in this module. Never raises —
    a failed or unconfigured send is logged and swallowed so it can never
    block the auth/security flow that triggered it (login, password reset,
    passkey registration, etc.)."""
    if not settings.email_configured:
        logger.info(
            "SMTP not configured — %s for %s was NOT sent (configure "
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
        with _force_ipv4_dns():
            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
                if settings.SMTP_USE_TLS:
                    server.starttls()
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.send_message(msg)
    except Exception:
        logger.exception("FAILED to send %s to %s", log_label, to_email)
        return

    logger.info("Sent %s to %s", log_label, to_email)


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
