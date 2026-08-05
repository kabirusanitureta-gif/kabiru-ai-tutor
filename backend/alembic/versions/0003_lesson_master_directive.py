"""add master directive lesson fields (assignment, challenge, summary, references, next lesson preview)

Revision ID: 0003_lesson_master_directive
Revises: 0002_lesson_extended
Create Date: 2026-08-05

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0003_lesson_master_directive"
down_revision: Union[str, None] = "0002_lesson_extended"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("lessons", sa.Column("assignment", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("challenge", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("summary", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("lesson_references", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("next_lesson_preview", sa.Text(), server_default=""))


def downgrade() -> None:
    op.drop_column("lessons", "next_lesson_preview")
    op.drop_column("lessons", "lesson_references")
    op.drop_column("lessons", "summary")
    op.drop_column("lessons", "challenge")
    op.drop_column("lessons", "assignment")
