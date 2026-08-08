"""webauthn credentials: Face ID / Touch ID / Windows Hello / security-key
passwordless login

Revision ID: 0009_webauthn_credentials
Revises: 0008_enterprise_security_foundation
Create Date: 2026-08-07

Purely additive: creates one new table, `webauthn_credentials`, and touches
nothing else. No existing column, table, or row is modified. Safe to run
against a production database with existing users, progress, notes,
certificates, or chat history — every current user simply has zero
registered passkeys until they add one from Settings, and keeps logging in
with email + password exactly as before in the meantime.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0009_webauthn_credentials"
down_revision: Union[str, None] = "0008_enterprise_security_foundation"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "webauthn_credentials",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("credential_id", sa.String(length=255), unique=True, index=True, nullable=False),
        sa.Column("public_key", sa.Text(), nullable=False),
        sa.Column("sign_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("transports", sa.String(length=120), nullable=True),
        sa.Column("device_name", sa.String(length=120), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("last_used_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("webauthn_credentials")
