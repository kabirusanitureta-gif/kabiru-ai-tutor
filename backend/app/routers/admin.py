from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session

from app.core.audit import log_action
from app.core.database import get_db
from app.core.deps import get_current_admin
from app.models.models import AuditLog, Course, Lesson, Quiz, Question, User
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
