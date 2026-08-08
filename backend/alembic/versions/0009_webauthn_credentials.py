"""add WebAuthn passkey credentials

Revision ID: 0009_webauthn_credentials
Revises: 0008_enterprise
Create Date: 2026-08-08
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0009_webauthn_credentials"
down_revision: Union[str, None] = "0008_enterprise"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "webauthn_credentials",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False,
        ),
        sa.Column("credential_id", sa.String(length=512), nullable=False, unique=True),
        sa.Column("public_key", sa.Text(), nullable=False),
        sa.Column("sign_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("device_name", sa.String(length=120), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )

    op.create_index(
        "ix_webauthn_credentials_user_id",
        "webauthn_credentials",
        ["user_id"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_webauthn_credentials_user_id",
        table_name="webauthn_credentials",
    )
    op.drop_table("webauthn_credentials")
