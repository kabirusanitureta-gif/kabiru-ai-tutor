"""
Minimal outgoing email for password-reset codes.

Uses only the Python standard library (smtplib/email) so no new dependency
is required. If SMTP_* settings aren't configured (settings.email_configured
is False), the message is logged instead of sent — this keeps local/dev/
offline setups working exactly as before, and never crashes the
forgot-password flow just because email isn't set up yet.
"""
import logging
import smtplib
from email.message import EmailMessage

from app.core.config import settings

logger = logging.getLogger("kabiru.email")


def send_password_reset_email(to_email: str, full_name: str, reset_code: str) -> None:
    subject = "Your Kabiru AI Tutor password reset code"
    body = (
        f"Hi {full_name},\n\n"
        f"Your password reset code is: {reset_code}\n\n"
        f"This code expires in {settings.PASSWORD_RESET_TOKEN_EXPIRE_MINUTES} minutes. "
        f"If you didn't request this, you can safely ignore this email.\n\n"
        f"— {settings.APP_NAME}"
    )

    if not settings.email_configured:
        # Safe no-op fallback: log only, never raise. Keeps the API response
        # generic regardless of email delivery status (see auth.py).
        logger.info(
            "SMTP not configured — password reset code for %s: %s "
            "(configure SMTP_HOST/SMTP_USER/SMTP_PASSWORD to send real emails)",
            to_email,
            reset_code,
        )
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
            if settings.SMTP_USE_TLS:
                server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
    except Exception:
        # Never let an SMTP outage break the request/leak whether the
        # account exists — log it server-side for ops to notice instead.
        logger.exception("Failed to send password reset email to %s", to_email)
