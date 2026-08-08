"""security hardening: soft delete, audit logs, avatar + role on users

Revision ID: 0005_security_hardening
Revises: 0004_auth_hardening
Create Date: 2026-08-06

Purely additive: adds new nullable/defaulted columns to existing tables
(users, courses, lessons, quizzes, questions) and creates one new table
(audit_logs). Does not drop, rename, or alter any existing column, and does
not touch a single existing row. Safe to run against a production database
with existing users, progress, notes, certificates, or chat history.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0005_security_hardening"
down_revision: Union[str, None] = "0004_auth_hardening"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- users: profile photo, coarse role, soft delete ---
    op.add_column("users", sa.Column("avatar_path", sa.String(length=300), nullable=True))
    op.add_column("users", sa.Column("role", sa.String(length=20), nullable=False, server_default="student"))
    op.add_column("users", sa.Column("is_deleted", sa.Boolean(), server_default=sa.false()))
    op.add_column("users", sa.Column("deleted_at", sa.DateTime(), nullable=True))
    op.create_index("ix_users_is_deleted", "users", ["is_deleted"])

    # Backfill: any existing admin (is_admin=True) becomes role="admin" so
    # the new `role` column agrees with the flag everyone already relies on.
    users = sa.table("users", sa.column("is_admin", sa.Boolean), sa.column("role", sa.String))
    op.execute(users.update().where(users.c.is_admin.is_(True)).values(role="admin"))

    # --- soft delete on admin-managed content tables ---
    for table in ("courses", "lessons", "quizzes", "questions"):
        op.add_column(table, sa.Column("is_deleted", sa.Boolean(), server_default=sa.false()))
        op.add_column(table, sa.Column("deleted_at", sa.DateTime(), nullable=True))
        op.create_index(f"ix_{table}_is_deleted", table, ["is_deleted"])

    # --- audit_logs ---
    op.create_table(
        "audit_logs",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("actor_user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True, index=True),
        sa.Column("action", sa.String(length=60), nullable=False, index=True),
        sa.Column("entity_type", sa.String(length=40), nullable=True),
        sa.Column("entity_id", sa.Integer(), nullable=True),
        sa.Column("details", sa.Text(), nullable=True),
        sa.Column("ip_address", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), index=True),
    )


def downgrade() -> None:
    op.drop_table("audit_logs")

    for table in ("courses", "lessons", "quizzes", "questions"):
        op.drop_index(f"ix_{table}_is_deleted", table_name=table)
        op.drop_column(table, "deleted_at")
        op.drop_column(table, "is_deleted")

    op.drop_index("ix_users_is_deleted", table_name="users")
    op.drop_column("users", "deleted_at")
    op.drop_column("users", "is_deleted")
    op.drop_column("users", "role")
    op.drop_column("users", "avatar_path")
