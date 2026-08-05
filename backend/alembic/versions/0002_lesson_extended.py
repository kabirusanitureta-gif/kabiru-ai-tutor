"""add professional lesson content fields

Revision ID: 0002_lesson_extended
Revises: 0001_initial
Create Date: 2026-08-05

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0002_lesson_extended"
down_revision: Union[str, None] = "0001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("lessons", sa.Column("real_world_project", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("common_mistakes", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("best_practices", sa.Text(), server_default=""))
    op.add_column("lessons", sa.Column("interview_questions", sa.Text(), server_default=""))


def downgrade() -> None:
    op.drop_column("lessons", "interview_questions")
    op.drop_column("lessons", "best_practices")
    op.drop_column("lessons", "common_mistakes")
    op.drop_column("lessons", "real_world_project")
