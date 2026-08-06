from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import Course, User
from app.schemas.content import CourseOut
from app.services.lesson_lock import get_locked_lesson_ids

router = APIRouter(prefix="/api/courses", tags=["courses"])


def _serialize_course(course: Course, locked_ids: set[int]) -> dict:
    return {
        "id": course.id,
        "slug": course.slug,
        "title": course.title,
        "description": course.description,
        "order_index": course.order_index,
        "lessons": [
            {
                "id": lesson.id,
                "slug": lesson.slug,
                "title": lesson.title,
                "order_index": lesson.order_index,
                "level": lesson.level,
                "locked": lesson.id in locked_ids,
            }
            for lesson in sorted(course.lessons, key=lambda l: l.order_index)
            if not lesson.is_deleted
        ],
    }


@router.get("", response_model=list[CourseOut])
def list_courses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    courses = db.query(Course).filter(Course.is_deleted.is_(False)).order_by(Course.order_index).all()
    locked_ids = get_locked_lesson_ids(db, current_user)
    return [_serialize_course(c, locked_ids) for c in courses]


@router.get("/{slug}", response_model=CourseOut)
def get_course(slug: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    course = db.query(Course).filter(Course.slug == slug, Course.is_deleted.is_(False)).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    locked_ids = get_locked_lesson_ids(db, current_user)
    return _serialize_course(course, locked_ids)
