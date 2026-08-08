"""
Database models for Kabiru AI Tutor.
"""
from datetime import datetime, date

from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, Date, ForeignKey, Float, UniqueConstraint
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

    # --- Email verification ---
    # Defaults to True at the Python/model level so anything that creates a
    # User without setting this explicitly (seed scripts, admin-created
    # accounts) keeps the old no-verification-needed behavior. /api/auth/register
    # is the one place that explicitly sets this to False for a brand new
    # signup. Existing rows are backfilled to True by the migration, so no
    # current user is ever asked to verify retroactively.
    is_verified = Column(Boolean, default=True, nullable=False)

    # Profile photo: only the relative path under the uploads dir is stored;
    # UserOut.avatar_url (see User.avatar_url property below) builds the
    # servable URL from it so routers never construct paths by hand.
    avatar_path = Column(String(300), nullable=True)

    # --- RBAC ---
    # Coarse role label alongside the existing is_admin flag (kept for
    # backward compatibility with every existing admin check). "super_admin"
    # is enforced to be unique across the whole table (see
    # app.core.rbac.ensure_single_super_admin) — everything else (course
    # editors, moderators, etc.) is just "admin" or "student" for now.
    role = Column(String(20), default="student", nullable=False)

    # --- Soft delete ---
    # Distinct from is_active (temporary disable): is_deleted marks an
    # account the user asked to close / an admin removed, while preserving
    # the row so progress, certificates, and history stay intact and FK
    # constraints never break. Soft-deleted users are excluded from normal
    # login and admin listings but never physically removed.
    is_deleted = Column(Boolean, default=False, index=True)
    deleted_at = Column(DateTime, nullable=True)

    # --- Enterprise Security foundation ---
    # Purely additive account-lifecycle / login-security fields. All are
    # nullable or carry a safe default so every existing row keeps working
    # exactly as before (existing users land as status="active",
    # is_approved=True — nobody already in the system is retroactively
    # locked out). Note: `role` (above) already existed pre-RBAC and keeps
    # its existing lowercase values (super_admin/admin/moderator/teacher/
    # student) untouched for backward compatibility with app.core.rbac.
    status = Column(String(20), default="active", nullable=False)  # pending/active/suspended/disabled
    is_approved = Column(Boolean, default=True, nullable=False)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    failed_login_attempts = Column(Integer, default=0, nullable=False)
    locked_until = Column(DateTime, nullable=True)
    last_login = Column(DateTime, nullable=True)
    last_login_ip = Column(String(64), nullable=True)
    last_login_device = Column(String(255), nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    approver = relationship("User", remote_side=[id], foreign_keys=[approved_by])

    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="user", cascade="all, delete-orphan")
    notes = relationship("Note", back_populates="user", cascade="all, delete-orphan")
    certificates = relationship("Certificate", back_populates="user", cascade="all, delete-orphan")
    chat_messages = relationship("ChatMessage", back_populates="user", cascade="all, delete-orphan")
    streak = relationship("StudyStreak", back_populates="user", uselist=False, cascade="all, delete-orphan")
    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")
    reset_tokens = relationship("PasswordResetToken", back_populates="user", cascade="all, delete-orphan")
    verification_tokens = relationship("EmailVerificationToken", back_populates="user", cascade="all, delete-orphan")
    webauthn_credentials = relationship(
        "WebAuthnCredential", back_populates="user", cascade="all, delete-orphan"
    )

    @property
    def avatar_url(self) -> str | None:
        """Servable URL for the profile photo, or None if the user hasn't set one."""
        if not self.avatar_path:
            return None
        return f"/uploads/avatars/{self.avatar_path}"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(60), unique=True, index=True, nullable=False)  # e.g. 'python'
    title = Column(String(150), nullable=False)
    description = Column(Text, default="")
    order_index = Column(Integer, default=0)

    # --- Soft delete (admin-managed content: never hard-deleted) ---
    is_deleted = Column(Boolean, default=False, index=True)
    deleted_at = Column(DateTime, nullable=True)

    lessons = relationship("Lesson", back_populates="course", cascade="all, delete-orphan", order_by="Lesson.order_index")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    slug = Column(String(80), index=True, nullable=False)
    title = Column(String(200), nullable=False)
    order_index = Column(Integer, default=0)
    level = Column(String(20), default="beginner")  # beginner/intermediate/advanced/expert/professional

    # --- Soft delete ---
    is_deleted = Column(Boolean, default=False, index=True)
    deleted_at = Column(DateTime, nullable=True)

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

    # --- Soft delete ---
    is_deleted = Column(Boolean, default=False, index=True)
    deleted_at = Column(DateTime, nullable=True)

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

    # --- Soft delete ---
    is_deleted = Column(Boolean, default=False, index=True)
    deleted_at = Column(DateTime, nullable=True)

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


class RefreshToken(Base):
    """
    Long-lived refresh tokens, stored as a SHA-256 hash (never plaintext) so a
    leaked database dump alone can't be used to impersonate users. Rotated on
    every use (old one revoked, new one issued) so a stolen token has a short
    useful window if the legitimate client keeps refreshing.
    """
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    token_hash = Column(String(64), unique=True, index=True, nullable=False)  # sha256 hex digest
    expires_at = Column(DateTime, nullable=False)
    revoked = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_agent = Column(String(255), nullable=True)

    user = relationship("User", back_populates="refresh_tokens")


class PasswordResetToken(Base):
    """
    Short-lived, single-use password reset codes. Stored hashed like refresh
    tokens. A row existing does NOT confirm the email was valid to API callers
    (the endpoint always responds the same way) — this table is only ever
    read internally during /reset-password.
    """
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    token_hash = Column(String(64), unique=True, index=True, nullable=False)  # sha256 hex digest
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reset_tokens")


class EmailVerificationToken(Base):
    """
    Short-lived, single-use 6-digit PIN sent to a new user's email at
    registration. Stored hashed, same pattern as PasswordResetToken. A row
    existing does NOT confirm anything to API callers by itself — /verify-email
    always checks hash + expiry + used before trusting it.
    """
    __tablename__ = "email_verification_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    token_hash = Column(String(64), unique=True, index=True, nullable=False)  # sha256 hex digest
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="verification_tokens")


class WebAuthnCredential(Base):
    """
    A registered WebAuthn authenticator (Face ID, Touch ID, Windows Hello,
    or a hardware security key) that can log this user in without a
    password. The biometric/PIN check itself always happens locally on the
    user's own device — this table never sees a fingerprint or a face, only
    the public half of a keypair the device generated, plus a signature
    counter used to detect cloned authenticators. Losing this table simply
    means affected users fall back to email + password; nobody is locked out.
    """
    __tablename__ = "webauthn_credentials"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    # base64url string exactly as the authenticator/browser reports it —
    # kept as the natural lookup key at login time (no re-encoding needed).
    credential_id = Column(String(255), unique=True, index=True, nullable=False)
    public_key = Column(Text, nullable=False)  # base64url-encoded COSE public key
    sign_count = Column(Integer, default=0, nullable=False)  # replay/clone detection
    transports = Column(String(120), nullable=True)  # e.g. "internal,hybrid"
    device_name = Column(String(120), nullable=True)  # user-facing label, e.g. "iPhone Face ID"
    created_at = Column(DateTime, default=datetime.utcnow)
    last_used_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="webauthn_credentials")


class AuditLog(Base):
    """
    Append-only trail of security-relevant and admin actions. Rows are never
    updated or deleted by the application — only inserted — so this table is
    safe to treat as a historical record even if the actor or target row is
    later soft-deleted.
    """
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    # Nullable: some events (e.g. a failed login for an email that doesn't
    # exist) have no authenticated actor yet.
    actor_user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    action = Column(String(60), nullable=False, index=True)  # e.g. "login_success", "lesson_deleted"
    entity_type = Column(String(40), nullable=True)  # e.g. "lesson", "user", "quiz"
    entity_id = Column(Integer, nullable=True)
    details = Column(Text, nullable=True)  # short human-readable context, not raw request bodies
    ip_address = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    # --- Enterprise Security foundation ---
    # Additive columns for the admin-facing "user management" audit trail
    # (distinct from the generic actor_user_id/entity_* fields above, which
    # app.core.audit.log_action already writes for every security event and
    # which stay untouched). admin_id/target_user_id/description let new
    # admin-on-user actions (approve, suspend, role change, etc.) be
    # recorded without disturbing the existing audit helper or its callers.
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    target_user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    description = Column(Text, nullable=True)

    actor = relationship("User", foreign_keys=[actor_user_id])
    admin = relationship("User", foreign_keys=[admin_id])
    target_user = relationship("User", foreign_keys=[target_user_id])


class RolePermission(Base):
    """
    Configurable override of the RBAC default permission matrix
    (see app.core.rbac.DEFAULT_PERMISSIONS). Starts empty; a row here only
    exists once an admin has explicitly turned a permission on/off for a
    role, so `has_permission()` falls back to the code defaults for every
    (role, permission) pair that has never been touched.
    """
    __tablename__ = "role_permissions"
    __table_args__ = (UniqueConstraint("role", "permission", name="uq_role_permission"),)

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(20), nullable=False, index=True)
    permission = Column(String(60), nullable=False)
    allowed = Column(Boolean, default=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class LoginHistory(Base):
    """
    Append-only record of every login attempt (success or failure), separate
    from AuditLog so the high-volume auth trail never crowds out the
    admin-action trail. Nothing else in the app reads or writes this table
    yet, so adding it is fully additive.
    """
    __tablename__ = "login_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    login_time = Column(DateTime, default=datetime.utcnow, index=True)
    logout_time = Column(DateTime, nullable=True)
    ip_address = Column(String(64), nullable=True)
    device = Column(String(255), nullable=True)
    browser = Column(String(100), nullable=True)
    operating_system = Column(String(100), nullable=True)
    success = Column(Boolean, default=True, nullable=False)

    user = relationship("User")


class SystemSettings(Base):
    """
    Singleton-style global settings row (application code should always
    read/create id=1). New table, referenced by nothing else yet, so adding
    it does not affect any existing route or model.
    """
    __tablename__ = "system_settings"

    id = Column(Integer, primary_key=True, index=True)
    registration_enabled = Column(Boolean, default=True, nullable=False)
    admin_approval_required = Column(Boolean, default=False, nullable=False)
    maintenance_mode = Column(Boolean, default=False, nullable=False)
    allow_password_reset = Column(Boolean, default=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
