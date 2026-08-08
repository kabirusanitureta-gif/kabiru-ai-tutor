import os
import shutil
import time
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy import func, text as sa_text
from sqlalchemy.orm import Session

from app.core.audit import log_action
from app.core.config import settings
from app.core.database import get_db
from app.core.deps import get_current_admin
from app.core.rbac import (
    DEFAULT_PERMISSIONS,
    PERMISSIONS,
    ROLES,
    ensure_single_super_admin,
    get_current_super_admin,
    has_permission,
    require_permission,
    sync_is_admin_flag,
)
from app.models.models import (
    AuditLog, Certificate, ChatMessage, Course, Lesson, Note,
    Question, Quiz, RolePermission, User,
)
from app.schemas.content import LessonOut, CourseOut, QuestionAdminOut

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/users", response_model=list[dict])
def list_users(
    include_deleted: bool = Query(False),
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin),
):
    query = db.query(User)
    if not include_deleted:
        query = query.filter(User.is_deleted.is_(False))
    users = query.all()
    return [
        {
            "id": u.id, "full_name": u.full_name, "email": u.email,
            "is_admin": u.is_admin, "role": u.role, "is_active": u.is_active,
            "is_deleted": u.is_deleted, "created_at": u.created_at,
        }
        for u in users
    ]


@router.patch("/users/{user_id}/toggle-active")
def toggle_user_active(user_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = not user.is_active
    db.commit()
    log_action(
        db, "user_active_toggled", actor=admin, entity_type="user", entity_id=user.id,
        details=f"is_active={user.is_active}", request=request,
    )
    return {"id": user.id, "is_active": user.is_active}


@router.delete("/users/{user_id}", status_code=204)
def soft_delete_user(user_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    """Soft-deletes a user account. The row, progress, notes, certificates,
    and chat history are all preserved -- only is_deleted/deleted_at are set,
    and the account can no longer log in (see get_current_user)."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role == "super_admin":
        raise HTTPException(status_code=400, detail="Cannot delete the Super Admin account")
    user.is_deleted = True
    user.deleted_at = datetime.utcnow()
    db.commit()
    log_action(db, "user_deleted", actor=admin, entity_type="user", entity_id=user.id, request=request)
    return None


@router.post("/users/{user_id}/restore")
def restore_user(user_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_deleted = False
    user.deleted_at = None
    db.commit()
    log_action(db, "user_restored", actor=admin, entity_type="user", entity_id=user.id, request=request)
    return {"id": user.id, "is_deleted": user.is_deleted}


@router.post("/courses", response_model=CourseOut, status_code=201)
def create_course(slug: str, title: str, request: Request, description: str = "", order_index: int = 0,
                   db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    if db.query(Course).filter(Course.slug == slug).first():
        raise HTTPException(status_code=400, detail="Course slug already exists")
    course = Course(slug=slug, title=title, description=description, order_index=order_index)
    db.add(course)
    db.commit()
    db.refresh(course)
    log_action(db, "course_created", actor=admin, entity_type="course", entity_id=course.id, details=slug, request=request)
    return course


@router.delete("/courses/{course_id}", status_code=204)
def delete_course(course_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    course = db.query(Course).filter(Course.id == course_id, Course.is_deleted.is_(False)).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.is_deleted = True
    course.deleted_at = datetime.utcnow()
    db.commit()
    log_action(db, "course_deleted", actor=admin, entity_type="course", entity_id=course.id, request=request)
    return None


@router.post("/courses/{course_id}/restore")
def restore_course(course_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.is_deleted = False
    course.deleted_at = None
    db.commit()
    log_action(db, "course_restored", actor=admin, entity_type="course", entity_id=course.id, request=request)
    return {"id": course.id, "is_deleted": course.is_deleted}


@router.post("/lessons", response_model=LessonOut, status_code=201)
def create_lesson(
    course_id: int, slug: str, title: str, explanation: str, examples: str,
    practice: str, mini_project: str, request: Request, order_index: int = 0, level: str = "beginner",
    db: Session = Depends(get_db), admin: User = Depends(get_current_admin),
):
    course = db.query(Course).filter(Course.id == course_id, Course.is_deleted.is_(False)).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    lesson = Lesson(
        course_id=course_id, slug=slug, title=title, order_index=order_index, level=level,
        explanation=explanation, examples=examples, practice=practice, mini_project=mini_project,
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    log_action(db, "lesson_created", actor=admin, entity_type="lesson", entity_id=lesson.id, details=slug, request=request)
    return lesson


@router.delete("/lessons/{lesson_id}", status_code=204)
def delete_lesson(lesson_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    """Soft delete: the lesson row, its quizzes/questions, and any student
    progress/notes referencing it are all preserved -- only hidden from
    normal listings (see courses.py / lessons.py filters)."""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.is_deleted.is_(False)).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    lesson.is_deleted = True
    lesson.deleted_at = datetime.utcnow()
    db.commit()
    log_action(db, "lesson_deleted", actor=admin, entity_type="lesson", entity_id=lesson.id, request=request)
    return None


@router.post("/lessons/{lesson_id}/restore")
def restore_lesson(lesson_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    lesson.is_deleted = False
    lesson.deleted_at = None
    db.commit()
    log_action(db, "lesson_restored", actor=admin, entity_type="lesson", entity_id=lesson.id, request=request)
    return {"id": lesson.id, "is_deleted": lesson.is_deleted}


@router.post("/quizzes", status_code=201)
def create_quiz(lesson_id: int, request: Request, title: str = "Lesson Quiz", passing_score: int = 70,
                 db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.is_deleted.is_(False)).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    quiz = Quiz(lesson_id=lesson_id, title=title, passing_score=passing_score)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    log_action(db, "quiz_created", actor=admin, entity_type="quiz", entity_id=quiz.id, request=request)
    return {"id": quiz.id, "lesson_id": quiz.lesson_id, "title": quiz.title}


@router.delete("/quizzes/{quiz_id}", status_code=204)
def delete_quiz(quiz_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id, Quiz.is_deleted.is_(False)).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    quiz.is_deleted = True
    quiz.deleted_at = datetime.utcnow()
    db.commit()
    log_action(db, "quiz_deleted", actor=admin, entity_type="quiz", entity_id=quiz.id, request=request)
    return None


@router.post("/questions", status_code=201)
def create_question(
    quiz_id: int, text: str, option_a: str, option_b: str, option_c: str, option_d: str,
    correct_option: str, request: Request, explanation: str = "",
    db: Session = Depends(get_db), admin: User = Depends(get_current_admin),
):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id, Quiz.is_deleted.is_(False)).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    if correct_option.lower() not in ("a", "b", "c", "d"):
        raise HTTPException(status_code=400, detail="correct_option must be a, b, c, or d")

    question = Question(
        quiz_id=quiz_id, text=text, option_a=option_a, option_b=option_b,
        option_c=option_c, option_d=option_d, correct_option=correct_option.lower(),
        explanation=explanation,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    log_action(db, "question_created", actor=admin, entity_type="question", entity_id=question.id, request=request)
    return QuestionAdminOut.model_validate(question)


@router.delete("/questions/{question_id}", status_code=204)
def delete_question(question_id: int, request: Request, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    question = db.query(Question).filter(Question.id == question_id, Question.is_deleted.is_(False)).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    question.is_deleted = True
    question.deleted_at = datetime.utcnow()
    db.commit()
    log_action(db, "question_deleted", actor=admin, entity_type="question", entity_id=question.id, request=request)
    return None


@router.get("/audit-logs")
def list_audit_logs(
    limit: int = Query(100, le=500),
    offset: int = Query(0, ge=0),
    action: str | None = None,
    entity_type: str | None = None,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin),
):
    query = db.query(AuditLog).order_by(AuditLog.created_at.desc())
    if action:
        query = query.filter(AuditLog.action == action)
    if entity_type:
        query = query.filter(AuditLog.entity_type == entity_type)
    rows = query.offset(offset).limit(limit).all()
    return [
        {
            "id": r.id,
            "actor_user_id": r.actor_user_id,
            "actor_name": r.actor.full_name if r.actor else None,
            "action": r.action,
            "entity_type": r.entity_type,
            "entity_id": r.entity_id,
            "details": r.details,
            "ip_address": r.ip_address,
            "created_at": r.created_at,
        }
        for r in rows
    ]


# ---------------------------------------------------------------------------
# RBAC: role assignment + configurable permission matrix
# ---------------------------------------------------------------------------

@router.get("/roles")
def list_roles(db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    """Every role, its effective permission set (default matrix overlaid
    with any explicit role_permissions rows), and how many active users
    currently hold it."""
    overrides = {(rp.role, rp.permission): rp.allowed for rp in db.query(RolePermission).all()}
    counts = dict(
        db.query(User.role, func.count(User.id))
        .filter(User.is_deleted.is_(False))
        .group_by(User.role)
        .all()
    )
    result = []
    for role in ROLES:
        if role == "super_admin":
            effective = set(PERMISSIONS)  # implicit: everything
        else:
            effective = set(DEFAULT_PERMISSIONS.get(role, set()))
            for perm in PERMISSIONS:
                key = (role, perm)
                if key in overrides:
                    if overrides[key]:
                        effective.add(perm)
                    else:
                        effective.discard(perm)
        result.append({
            "role": role,
            "user_count": counts.get(role, 0),
            "permissions": sorted(effective),
        })
    return result


@router.get("/permissions")
def list_all_permissions():
    """Full permission catalog, used to render the permission matrix editor."""
    return {"permissions": PERMISSIONS, "roles": [r for r in ROLES if r != "super_admin"]}


@router.put("/permissions/{role}/{permission}")
def set_role_permission(
    role: str, permission: str, allowed: bool, request: Request,
    db: Session = Depends(get_db), admin: User = Depends(get_current_super_admin),
):
    """Override a single (role, permission) pair. Super Admin only -- the
    permission matrix itself is security-sensitive, so only the one account
    guaranteed to be trusted can edit it."""
    if role not in ROLES or role == "super_admin":
        raise HTTPException(status_code=400, detail="Invalid role")
    if permission not in PERMISSIONS:
        raise HTTPException(status_code=400, detail="Invalid permission")

    row = (
        db.query(RolePermission)
        .filter(RolePermission.role == role, RolePermission.permission == permission)
        .first()
    )
    if row is None:
        row = RolePermission(role=role, permission=permission, allowed=allowed)
        db.add(row)
    else:
        row.allowed = allowed
        row.updated_at = datetime.utcnow()
    db.commit()
    log_action(
        db, "role_permission_updated", actor=admin, entity_type="role_permission",
        details=f"{role}.{permission}={allowed}", request=request,
    )
    return {"role": role, "permission": permission, "allowed": allowed}


@router.patch("/users/{user_id}/role")
def change_user_role(
    user_id: int, role: str, request: Request,
    db: Session = Depends(get_db), admin: User = Depends(get_current_admin),
):
    """Assigns a new role to a user. Only Super Admin can grant or revoke
    the super_admin role itself (and there can only ever be one); any admin
    with users.manage can assign the other four roles."""
    if role not in ROLES:
        raise HTTPException(status_code=400, detail=f"role must be one of {ROLES}")

    target = db.query(User).filter(User.id == user_id, User.is_deleted.is_(False)).first()
    if not target:
        raise HTTPException(status_code=404, detail="User not found")

    if role == "super_admin" or target.role == "super_admin":
        if admin.role != "super_admin":
            raise HTTPException(status_code=403, detail="Only the Super Admin can change the Super Admin role")
    elif not (admin.is_admin and admin.role in ("admin", "super_admin")) and not has_permission(db, admin, "users.manage"):
        raise HTTPException(status_code=403, detail="Missing permission: users.manage")

    if role == "super_admin":
        ensure_single_super_admin(db, candidate_user_id=target.id)

    old_role = target.role
    target.role = role
    sync_is_admin_flag(target)
    db.commit()
    log_action(
        db, "user_role_changed", actor=admin, entity_type="user", entity_id=target.id,
        details=f"{old_role} -> {role}", request=request,
    )
    return {"id": target.id, "role": target.role, "is_admin": target.is_admin}


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------

def _dir_size_bytes(path: str) -> int:
    total = 0
    if not os.path.isdir(path):
        return 0
    for dirpath, _dirnames, filenames in os.walk(path):
        for name in filenames:
            try:
                total += os.path.getsize(os.path.join(dirpath, name))
            except OSError:
                continue
    return total


@router.get("/dashboard")
def dashboard_stats(db: Session = Depends(get_db), admin: User = Depends(require_permission("dashboard.view"))):
    """Aggregate counts for the admin dashboard: users, content, AI usage,
    storage, and a lightweight DB health check. All counts exclude
    soft-deleted rows where the model supports it, matching what normal
    users can actually see."""
    now = datetime.utcnow()
    since_24h = now - timedelta(hours=24)
    since_5min = now - timedelta(minutes=5)

    db_start = time.monotonic()
    try:
        db.execute(sa_text("SELECT 1"))
        db_healthy = True
        db_error = None
    except Exception as exc:  # pragma: no cover - defensive
        db_healthy = False
        db_error = str(exc)
    db_latency_ms = round((time.monotonic() - db_start) * 1000, 2)

    total_storage_bytes = 0
    if os.path.isdir(settings.UPLOAD_DIR):
        try:
            usage = shutil.disk_usage(settings.UPLOAD_DIR)
            total_storage_bytes = _dir_size_bytes(settings.UPLOAD_DIR)
        except OSError:
            usage = None
    else:
        usage = None

    return {
        "users": {
            "total": db.query(func.count(User.id)).filter(User.is_deleted.is_(False)).scalar(),
            "active": db.query(func.count(User.id)).filter(User.is_deleted.is_(False), User.is_active.is_(True)).scalar(),
            "online_last_5min": (
                db.query(func.count(func.distinct(ChatMessage.user_id)))
                .filter(ChatMessage.created_at >= since_5min)
                .scalar()
                if hasattr(ChatMessage, "created_at") else 0
            ),
            "new_last_24h": db.query(func.count(User.id)).filter(User.created_at >= since_24h).scalar(),
            "by_role": dict(db.query(User.role, func.count(User.id)).filter(User.is_deleted.is_(False)).group_by(User.role).all()),
        },
        "content": {
            "courses": db.query(func.count(Course.id)).filter(Course.is_deleted.is_(False)).scalar(),
            "lessons": db.query(func.count(Lesson.id)).filter(Lesson.is_deleted.is_(False)).scalar(),
            "quizzes": db.query(func.count(Quiz.id)).filter(Quiz.is_deleted.is_(False)).scalar(),
            "certificates": db.query(func.count(Certificate.id)).scalar(),
            "notes": db.query(func.count(Note.id)).scalar(),
        },
        "ai_usage": {
            "total_chat_messages": db.query(func.count(ChatMessage.id)).scalar(),
            "messages_last_24h": (
                db.query(func.count(ChatMessage.id)).filter(ChatMessage.created_at >= since_24h).scalar()
                if hasattr(ChatMessage, "created_at") else None
            ),
        },
        "storage": {
            "uploads_bytes": total_storage_bytes,
            "disk_free_bytes": usage.free if usage else None,
            "disk_total_bytes": usage.total if usage else None,
        },
        "database": {
            "healthy": db_healthy,
            "latency_ms": db_latency_ms,
            "error": db_error,
            "engine": "sqlite" if settings.using_sqlite else "postgres",
        },
    }
