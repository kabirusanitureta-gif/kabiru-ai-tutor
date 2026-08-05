"""
Database models for Kabiru AI Tutor.
"""
from datetime import datetime, date

from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, Date, ForeignKey, Float
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(120), nullable=False)
    email = Column(String(180), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    preferred_language = Column(String(10), default="en")  # 'en' or 'ha'
    theme = Column(String(10), default="light")  # 'light' or 'dark'
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="user", cascade="all, delete-orphan")
    notes = relationship("Note", back_populates="user", cascade="all, delete-orphan")
    certificates = relationship("Certificate", back_populates="user", cascade="all, delete-orphan")
    chat_messages = relationship("ChatMessage", back_populates="user", cascade="all, delete-orphan")
    streak = relationship("StudyStreak", back_populates="user", uselist=False, cascade="all, delete-orphan")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(60), unique=True, index=True, nullable=False)  # e.g. 'python'
    title = Column(String(150), nullable=False)
    description = Column(Text, default="")
    order_index = Column(Integer, default=0)

    lessons = relationship("Lesson", back_populates="course", cascade="all, delete-orphan", order_by="Lesson.order_index")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    slug = Column(String(80), index=True, nullable=False)
    title = Column(String(200), nullable=False)
    order_index = Column(Integer, default=0)
    level = Column(String(20), default="beginner")  # beginner/intermediate/advanced/expert/professional

    explanation = Column(Text, default="")
    examples = Column(Text, default="")
    practice = Column(Text, default="")
    mini_project = Column(Text, default="")
    # Professional curriculum fields (added for full Coursera/Udemy-style depth):
    real_world_project = Column(Text, default="")
    common_mistakes = Column(Text, default="")
    best_practices = Column(Text, default="")
    interview_questions = Column(Text, default="")
    # Master Directive fields (full 14-part professional lesson structure):
    assignment = Column(Text, default="")
    challenge = Column(Text, default="")
    summary = Column(Text, default="")
    lesson_references = Column(Text, default="")  # "references" is a reserved-ish name; avoid shadowing
    next_lesson_preview = Column(Text, default="")

    course = relationship("Course", back_populates="lessons")
    quizzes = relationship("Quiz", back_populates="lesson", cascade="all, delete-orphan")
    progress_entries = relationship("Progress", back_populates="lesson", cascade="all, delete-orphan")


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    title = Column(String(200), default="Lesson Quiz")
    passing_score = Column(Integer, default=70)  # percent

    lesson = relationship("Lesson", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="quiz", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    text = Column(Text, nullable=False)
    option_a = Column(String(300), nullable=False)
    option_b = Column(String(300), nullable=False)
    option_c = Column(String(300), nullable=False)
    option_d = Column(String(300), nullable=False)
    correct_option = Column(String(1), nullable=False)  # 'a' | 'b' | 'c' | 'd'
    explanation = Column(Text, default="")

    quiz = relationship("Quiz", back_populates="questions")


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    score_percent = Column(Float, default=0.0)
    passed = Column(Boolean, default=False)
    answers_json = Column(Text, default="{}")  # {"question_id": "a", ...}
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="attempts")
    quiz = relationship("Quiz", back_populates="attempts")


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    completed = Column(Boolean, default=False)
    quiz_passed = Column(Boolean, default=False)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="progress")
    lesson = relationship("Lesson", back_populates="progress_entries")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=True)
    title = Column(String(200), default="Untitled note")
    content = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="notes")


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    certificate_code = Column(String(40), unique=True, index=True, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String(300), nullable=True)

    user = relationship("User", back_populates="certificates")
    course = relationship("Course")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String(10), default="user")  # 'user' | 'assistant'
    content = Column(Text, nullable=False)
    language = Column(String(10), default="en")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="chat_messages")


class StudyStreak(Base):
    __tablename__ = "study_streaks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_active_date = Column(Date, default=date.today)

    user = relationship("User", back_populates="streak")
