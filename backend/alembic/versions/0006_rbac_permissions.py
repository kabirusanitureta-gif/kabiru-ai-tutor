"""rbac: configurable role_permissions table

Revision ID: 0006_rbac_permissions
Revises: 0005_security_hardening
Create Date: 2026-08-06

Purely additive: creates one new table (role_permissions). Does not touch
users, courses, lessons, quizzes, questions, or any other existing table or
row. The `role` column on users already exists (0005) and already supports
any of the five RBAC role strings, so no user data migration is needed here.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0006_rbac_permissions"
down_revision: Union[str, None] = "0005_security_hardening"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "role_permissions",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("role", sa.String(length=20), nullable=False, index=True),
        sa.Column("permission", sa.String(length=60), nullable=False),
        sa.Column("allowed", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now()),
        sa.UniqueConstraint("role", "permission", name="uq_role_permission"),
    )


def downgrade() -> None:
    op.drop_table("role_permissions")
