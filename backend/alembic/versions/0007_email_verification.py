"""email verification: is_verified on users + email_verification_tokens

Revision ID: 0007_email_verification
Revises: 0006_rbac_permissions
Create Date: 2026-08-06

Purely additive: adds one new nullable-with-default column to the existing
`users` table and creates one new table. Does not drop, rename, or alter
any existing column, and does not touch a single existing row's data other
than backfilling the new column to True (so no current user is ever asked
to verify retroactively — only brand new registrations start unverified).
Safe to run against a production database with existing users, progress,
notes, certificates, or chat history.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0007_email_verification"
down_revision: Union[str, None] = "0006_rbac_permissions"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("is_verified", sa.Boolean(), nullable=False, server_default=sa.true()),
    )

    op.create_table(
        "email_verification_tokens",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("token_hash", sa.String(length=64), unique=True, index=True, nullable=False),
        sa.Column("expires_at", sa.DateTime(), nullable=False),
        sa.Column("used", sa.Boolean(), server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("email_verification_tokens")
    op.drop_column("users", "is_verified")
