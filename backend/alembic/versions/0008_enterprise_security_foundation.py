"""enterprise security foundation: user lifecycle fields, login_history,
audit_logs admin/target/description columns, system_settings

Revision ID: 0008_enterprise_security_foundation
Revises: 0007_email_verification
Create Date: 2026-08-06

Purely additive:
  - adds new nullable/defaulted columns to the existing `users` table
    (status, is_approved, approved_by, approved_at, failed_login_attempts,
    locked_until, last_login, last_login_ip, last_login_device, updated_at)
  - adds new nullable columns to the existing `audit_logs` table
    (admin_id, target_user_id, description) alongside its current columns
  - creates two new tables: `login_history`, `system_settings`

Does not drop, rename, or alter any existing column or table, and does not
touch a single existing row's data other than the safe backfill below.
Existing users are backfilled to status="active", is_approved=True so no
current user is retroactively locked out or unapproved. The existing
`role` column and its values (super_admin/admin/moderator/teacher/student)
are left completely untouched. Safe to run against a production database
with existing users, progress, notes, certificates, or chat history.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0008_enterprise_security_foundation"
down_revision: Union[str, None] = "0007_email_verification"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- users: account lifecycle / login-security fields ---
    op.add_column("users", sa.Column("status", sa.String(length=20), nullable=False, server_default="active"))
    op.add_column("users", sa.Column("is_approved", sa.Boolean(), nullable=False, server_default=sa.true()))
    op.add_column("users", sa.Column("approved_by", sa.Integer(), sa.ForeignKey("users.id"), nullable=True))
    op.add_column("users", sa.Column("approved_at", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("failed_login_attempts", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("users", sa.Column("locked_until", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("last_login", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("last_login_ip", sa.String(length=64), nullable=True))
    op.add_column("users", sa.Column("last_login_device", sa.String(length=255), nullable=True))
    op.add_column("users", sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now()))

    # --- audit_logs: additive admin-action columns (existing columns untouched) ---
    op.add_column("audit_logs", sa.Column("admin_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True))
    op.add_column("audit_logs", sa.Column("target_user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True))
    op.add_column("audit_logs", sa.Column("description", sa.Text(), nullable=True))
    op.create_index("ix_audit_logs_admin_id", "audit_logs", ["admin_id"])
    op.create_index("ix_audit_logs_target_user_id", "audit_logs", ["target_user_id"])

    # --- login_history ---
    op.create_table(
        "login_history",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True, index=True),
        sa.Column("login_time", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("logout_time", sa.DateTime(), nullable=True),
        sa.Column("ip_address", sa.String(length=64), nullable=True),
        sa.Column("device", sa.String(length=255), nullable=True),
        sa.Column("browser", sa.String(length=100), nullable=True),
        sa.Column("operating_system", sa.String(length=100), nullable=True),
        sa.Column("success", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.create_index("ix_login_history_login_time", "login_history", ["login_time"])

    # --- system_settings ---
    op.create_table(
        "system_settings",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("registration_enabled", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("admin_approval_required", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("maintenance_mode", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("allow_password_reset", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now()),
    )
    # Seed the single settings row so the app can always assume id=1 exists.
    system_settings = sa.table(
        "system_settings",
        sa.column("id", sa.Integer),
        sa.column("registration_enabled", sa.Boolean),
        sa.column("admin_approval_required", sa.Boolean),
        sa.column("maintenance_mode", sa.Boolean),
        sa.column("allow_password_reset", sa.Boolean),
    )
    op.execute(
        system_settings.insert().values(
            id=1,
            registration_enabled=True,
            admin_approval_required=False,
            maintenance_mode=False,
            allow_password_reset=True,
        )
    )


def downgrade() -> None:
    op.drop_table("system_settings")

    op.drop_index("ix_login_history_login_time", table_name="login_history")
    op.drop_table("login_history")

    op.drop_index("ix_audit_logs_target_user_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_admin_id", table_name="audit_logs")
    op.drop_column("audit_logs", "description")
    op.drop_column("audit_logs", "target_user_id")
    op.drop_column("audit_logs", "admin_id")

    op.drop_column("users", "updated_at")
    op.drop_column("users", "last_login_device")
    op.drop_column("users", "last_login_ip")
    op.drop_column("users", "last_login")
    op.drop_column("users", "locked_until")
    op.drop_column("users", "failed_login_attempts")
    op.drop_column("users", "approved_at")
    op.drop_column("users", "approved_by")
    op.drop_column("users", "is_approved")
    op.drop_column("users", "status")
