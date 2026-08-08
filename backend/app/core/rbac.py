"""
Role-Based Access Control.

Five roles: super_admin, admin, moderator, teacher, student.

Design notes (read before changing):
- The existing `User.is_admin` boolean and `User.role` string both already
  exist in production (see 0005_security_hardening). We never remove
  `is_admin` -- every dependency that already checked it keeps working.
  Instead, `is_admin` is kept in sync whenever `role` changes (see
  `sync_is_admin_flag`), so old code paths and new role-aware code paths
  never disagree.
- Permissions are "configurable" via the `role_permissions` table: it
  starts empty, and `has_permission` falls back to DEFAULT_PERMISSIONS
  when there's no explicit row for a (role, permission) pair. An admin can
  override a single permission for a single role without redefining the
  whole matrix.
- Only one super_admin may exist at a time. `ensure_single_super_admin`
  is the single place that rule is enforced -- call it before committing
  any role change to "super_admin".
"""
from __future__ import annotations

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import RolePermission, User

ROLES: list[str] = ["super_admin", "admin", "moderator", "teacher", "student"]

# Every permission string used anywhere in the admin surface. Keep this in
# sync with what routers actually check via `require_permission`.
PERMISSIONS: list[str] = [
    "users.view",
    "users.manage",       # activate/deactivate/soft-delete/restore/change role
    "courses.manage",
    "lessons.manage",
    "quizzes.manage",
    "notes.moderate",
    "certificates.view",
    "chat.moderate",
    "audit_logs.view",
    "reports.view",
    "dashboard.view",
    "roles.manage",       # edit the permission matrix itself (super_admin only, enforced separately)
]

# Default permission matrix. super_admin implicitly has everything (checked
# in code, not listed here, so it can never be misconfigured away).
DEFAULT_PERMISSIONS: dict[str, set[str]] = {
    "admin": {
        "users.view", "users.manage", "courses.manage", "lessons.manage",
        "quizzes.manage", "notes.moderate", "certificates.view",
        "chat.moderate", "audit_logs.view", "reports.view", "dashboard.view",
    },
    "moderator": {
        "users.view", "notes.moderate", "chat.moderate", "reports.view",
        "dashboard.view",
    },
    "teacher": {
        "courses.manage", "lessons.manage", "quizzes.manage",
        "certificates.view", "dashboard.view",
    },
    "student": set(),
}


def sync_is_admin_flag(user: User) -> None:
    """Keeps the legacy `is_admin` boolean consistent with `role`. Call this
    any time `role` is set, before commit. Never breaks old `is_admin`-only
    checks elsewhere in the codebase."""
    user.is_admin = user.role in ("admin", "super_admin")


def ensure_single_super_admin(db: Session, candidate_user_id: int) -> None:
    """Raises 400 if promoting candidate_user_id to super_admin would result
    in more than one super_admin existing. Call before assigning the role."""
    existing = (
        db.query(User)
        .filter(User.role == "super_admin", User.id != candidate_user_id, User.is_deleted.is_(False))
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A Super Admin already exists ({existing.email}). Demote them first.",
        )


def has_permission(db: Session, user: User, permission: str) -> bool:
    if user.role == "super_admin":
        return True
    override = (
        db.query(RolePermission)
        .filter(RolePermission.role == user.role, RolePermission.permission == permission)
        .first()
    )
    if override is not None:
        return override.allowed
    return permission in DEFAULT_PERMISSIONS.get(user.role, set())


def require_permission(permission: str):
    """Dependency factory: `Depends(require_permission("users.manage"))`.
    is_admin=True always passes (backward compatibility for any account
    that predates the role column / was set up before RBAC existed)."""

    def _dependency(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db),
    ) -> User:
        if current_user.is_admin and current_user.role in ("admin", "super_admin"):
            return current_user
        if has_permission(db, current_user, permission):
            return current_user
        raise HTTPException(status_code=403, detail=f"Missing permission: {permission}")

    return _dependency


def require_roles(*roles: str):
    """Dependency factory restricting access to specific roles, e.g.
    `Depends(require_roles("super_admin"))`."""

    def _dependency(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in roles:
            raise HTTPException(status_code=403, detail=f"Requires role: {' or '.join(roles)}")
        return current_user

    return _dependency


def get_current_super_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != "super_admin":
        raise HTTPException(status_code=403, detail="Super Admin access required")
    return current_user
