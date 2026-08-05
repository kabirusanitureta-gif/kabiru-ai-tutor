from datetime import date, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import Progress, User, Course, Lesson, StudyStreak
from app.schemas.content import ProgressOut

router = APIRouter(prefix="/api/progress", tags=["progress"])


@router.get("/mine", response_model=list[ProgressOut])
def my_progress(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Progress).filter(Progress.user_id == current_user.id).all()


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    courses = db.query(Course).all()
    all_progress = {p.lesson_id: p for p in db.query(Progress).filter(Progress.user_id == current_user.id).all()}

    course_summaries = []
    total_lessons = 0
    total_completed = 0

    for course in courses:
        lesson_ids = [l.id for l in course.lessons]
        completed = sum(1 for lid in lesson_ids if all_progress.get(lid) and all_progress[lid].completed)
        total = len(lesson_ids)
        total_lessons += total
        total_completed += completed
        percent = round((completed / total) * 100, 1) if total > 0 else 0.0
        course_summaries.append({
            "course_slug": course.slug,
            "course_title": course.title,
            "completed_lessons": completed,
            "total_lessons": total,
            "percent_complete": percent,
        })

    streak = db.query(StudyStreak).filter(StudyStreak.user_id == current_user.id).first()

    return {
        "overall_percent": round((total_completed / total_lessons) * 100, 1) if total_lessons > 0 else 0.0,
        "total_completed_lessons": total_completed,
        "total_lessons": total_lessons,
        "courses": course_summaries,
        "current_streak": streak.current_streak if streak else 0,
        "longest_streak": streak.longest_streak if streak else 0,
    }


@router.post("/streak/ping")
def ping_streak(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Call this once per day of activity (e.g. on login or first lesson view) to update the streak."""
    streak = db.query(StudyStreak).filter(StudyStreak.user_id == current_user.id).first()
    if not streak:
        streak = StudyStreak(user_id=current_user.id, current_streak=1, longest_streak=1, last_active_date=date.today())
        db.add(streak)
        db.commit()
        db.refresh(streak)
        return {"current_streak": streak.current_streak, "longest_streak": streak.longest_streak}

    today = date.today()
    if streak.last_active_date == today:
        pass  # already counted today
    elif streak.last_active_date == today - timedelta(days=1):
        streak.current_streak += 1
        streak.longest_streak = max(streak.longest_streak, streak.current_streak)
        streak.last_active_date = today
    else:
        streak.current_streak = 1
        streak.last_active_date = today

    db.commit()
    db.refresh(streak)
    return {"current_streak": streak.current_streak, "longest_streak": streak.longest_streak}
