"""
Audit logging helper.

Call `log_action(...)` after any security-relevant or admin event. Failures
here never take down the request that triggered them — logging is best
effort and must not block registration, login, or admin actions.
"""
import logging

from fastapi import Request
from sqlalchemy.orm import Session

from app.models.models import AuditLog, User

logger = logging.getLogger("kabiru.audit")


def _client_ip(request: Request | None) -> str | None:
    if request is None:
        return None
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else None


def log_action(
    db: Session,
    action: str,
    actor: User | None = None,
    entity_type: str | None = None,
    entity_id: int | None = None,
    details: str | None = None,
    request: Request | None = None,
) -> None:
    """Insert one audit_logs row. Commits immediately so a later rollback in
    the caller's transaction can't silently erase the record of what happened."""
    try:
        row = AuditLog(
            actor_user_id=actor.id if actor else None,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            details=details,
            ip_address=_client_ip(request),
        )
        db.add(row)
        db.commit()
    except Exception:
        # Never let audit logging break the actual request.
        db.rollback()
        logger.exception("Failed to write audit log for action=%s", action)
