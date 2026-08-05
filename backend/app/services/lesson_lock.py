"""
Lesson Lock Service.

Enforces the platform's strict-sequence rule: a student may not access
Lesson N+1 until Lesson N has been marked complete AND its quiz has been
passed. This is the server-side source of truth for locking — the frontend
only reflects it, it never decides it. Admin accounts bypass the lock so
staff can preview any lesson while building/reviewing curriculum.
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.models import Course, Lesson, Progress, User


def get_global_lesson_order(db: Session) -> list[Lesson]:
    """All lessons across all courses, in the single strict learning sequence
    (course order first, then lesson order within each course)."""
    return (
        db.query(Lesson)
        .join(Course, Lesson.course_id == Course.id)
        .order_by(Course.order_index, Lesson.order_index)
        .all()
    )


def get_locked_lesson_ids(db: Session, user: User) -> set[int]:
    """Return the IDs of every lesson this user cannot yet open."""
    if user.is_admin:
        return set()

    ordered_lessons = get_global_lesson_order(db)
    progress_by_lesson = {
        p.lesson_id: p
        for p in db.query(Progress).filter(Progress.user_id == user.id).all()
    }

    locked_ids: set[int] = set()
    previous_fully_done = True  # the first lesson in the curriculum is always open
    for lesson in ordered_lessons:
        if not previous_fully_done:
            locked_ids.add(lesson.id)

        progress = progress_by_lesson.get(lesson.id)
        previous_fully_done = bool(progress and progress.completed and progress.quiz_passed)

    return locked_ids


def assert_lesson_unlocked(db: Session, user: User, lesson: Lesson) -> None:
    """Raise 403 if the user has not yet earned access to this lesson."""
    if lesson.id in get_locked_lesson_ids(db, user):
        raise HTTPException(
            status_code=403,
            detail=(
                "This lesson is locked. Finish the previous lesson and pass its quiz "
                "first. / An kulle wannan darasi. Kammala darasi na baya kuma ka ci "
                "jarabawarsa kafin ka ci gaba."
            ),
        )
