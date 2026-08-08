from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import Lesson, Progress, User, Course
from app.schemas.content import LessonOut
from app.services.lesson_lock import assert_lesson_unlocked

router = APIRouter(prefix="/api/lessons", tags=["lessons"])


@router.get("/search", response_model=list[LessonOut])
def search_lessons(q: str = Query(min_length=1), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    results = (
        db.query(Lesson)
        .filter(
            Lesson.is_deleted.is_(False),
            or_(Lesson.title.ilike(f"%{q}%"), Lesson.explanation.ilike(f"%{q}%")),
        )
        .limit(30)
        .all()
    )
    return results


@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.is_deleted.is_(False)).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    assert_lesson_unlocked(db, current_user, lesson)

    # Attach the current user's saved progress so the frontend can resume
    # correctly (e.g. show "Completed" instead of resetting on every visit).
    progress = (
        db.query(Progress)
        .filter(Progress.user_id == current_user.id, Progress.lesson_id == lesson_id)
        .first()
    )
    lesson.is_completed = bool(progress and progress.completed)
    return lesson


@router.post("/{lesson_id}/complete")
def mark_lesson_complete(lesson_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.is_deleted.is_(False)).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    assert_lesson_unlocked(db, current_user, lesson)

    progress = (
        db.query(Progress)
        .filter(Progress.user_id == current_user.id, Progress.lesson_id == lesson_id)
        .first()
    )
    if not progress:
        progress = Progress(user_id=current_user.id, lesson_id=lesson_id)
        db.add(progress)

    progress.completed = True
    progress.completed_at = datetime.utcnow()
    db.commit()
    return {"status": "ok", "lesson_id": lesson_id}


@router.get("/recommend/next")
def recommend_next_lesson(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Recommends the next lesson: the lowest order_index lesson, across all
    courses, that the student has not yet completed with a passed quiz.
    """
    completed_ids = {
        p.lesson_id for p in
        db.query(Progress).filter(Progress.user_id == current_user.id, Progress.completed == True).all()
    }

    courses = db.query(Course).filter(Course.is_deleted.is_(False)).order_by(Course.order_index).all()
    for course in courses:
        for lesson in sorted(course.lessons, key=lambda l: l.order_index):
            if lesson.is_deleted:
                continue
            if lesson.id not in completed_ids:
                return {
                    "lesson_id": lesson.id,
                    "course_slug": course.slug,
                    "course_title": course.title,
                    "lesson_title": lesson.title,
                    "reason": "Next uncompleted lesson in curriculum order",
                }

    return {"lesson_id": None, "message": "All available lessons completed. Great work!"}
