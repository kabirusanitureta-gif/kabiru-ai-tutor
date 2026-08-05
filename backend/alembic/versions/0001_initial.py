"""initial schema

Revision ID: 0001_initial
Revises:
Create Date: 2026-08-01

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("full_name", sa.String(120), nullable=False),
        sa.Column("email", sa.String(180), nullable=False, unique=True, index=True),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("preferred_language", sa.String(10), server_default="en"),
        sa.Column("theme", sa.String(10), server_default="light"),
        sa.Column("is_admin", sa.Boolean(), server_default=sa.false()),
        sa.Column("is_active", sa.Boolean(), server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "courses",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("slug", sa.String(60), nullable=False, unique=True, index=True),
        sa.Column("title", sa.String(150), nullable=False),
        sa.Column("description", sa.Text(), server_default=""),
        sa.Column("order_index", sa.Integer(), server_default="0"),
    )

    op.create_table(
        "lessons",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("slug", sa.String(80), nullable=False, index=True),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("order_index", sa.Integer(), server_default="0"),
        sa.Column("level", sa.String(20), server_default="beginner"),
        sa.Column("explanation", sa.Text(), server_default=""),
        sa.Column("examples", sa.Text(), server_default=""),
        sa.Column("practice", sa.Text(), server_default=""),
        sa.Column("mini_project", sa.Text(), server_default=""),
    )

    op.create_table(
        "quizzes",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("lesson_id", sa.Integer(), sa.ForeignKey("lessons.id"), nullable=False),
        sa.Column("title", sa.String(200), server_default="Lesson Quiz"),
        sa.Column("passing_score", sa.Integer(), server_default="70"),
    )

    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("quiz_id", sa.Integer(), sa.ForeignKey("quizzes.id"), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("option_a", sa.String(300), nullable=False),
        sa.Column("option_b", sa.String(300), nullable=False),
        sa.Column("option_c", sa.String(300), nullable=False),
        sa.Column("option_d", sa.String(300), nullable=False),
        sa.Column("correct_option", sa.String(1), nullable=False),
        sa.Column("explanation", sa.Text(), server_default=""),
    )

    op.create_table(
        "attempts",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("quiz_id", sa.Integer(), sa.ForeignKey("quizzes.id"), nullable=False),
        sa.Column("score_percent", sa.Float(), server_default="0.0"),
        sa.Column("passed", sa.Boolean(), server_default=sa.false()),
        sa.Column("answers_json", sa.Text(), server_default="{}"),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "progress",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("lesson_id", sa.Integer(), sa.ForeignKey("lessons.id"), nullable=False),
        sa.Column("completed", sa.Boolean(), server_default=sa.false()),
        sa.Column("quiz_passed", sa.Boolean(), server_default=sa.false()),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "notes",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("lesson_id", sa.Integer(), sa.ForeignKey("lessons.id"), nullable=True),
        sa.Column("title", sa.String(200), server_default="Untitled note"),
        sa.Column("content", sa.Text(), server_default=""),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "certificates",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("certificate_code", sa.String(40), nullable=False, unique=True, index=True),
        sa.Column("issued_at", sa.DateTime(), nullable=True),
        sa.Column("file_path", sa.String(300), nullable=True),
    )

    op.create_table(
        "chat_messages",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("role", sa.String(10), server_default="user"),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("language", sa.String(10), server_default="en"),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "study_streaks",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False, unique=True),
        sa.Column("current_streak", sa.Integer(), server_default="0"),
        sa.Column("longest_streak", sa.Integer(), server_default="0"),
        sa.Column("last_active_date", sa.Date(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("study_streaks")
    op.drop_table("chat_messages")
    op.drop_table("certificates")
    op.drop_table("notes")
    op.drop_table("progress")
    op.drop_table("attempts")
    op.drop_table("questions")
    op.drop_table("quizzes")
    op.drop_table("lessons")
    op.drop_table("courses")
    op.drop_table("users")
