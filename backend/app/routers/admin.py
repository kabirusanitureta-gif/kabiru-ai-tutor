from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_admin
from app.models.models import Course, Lesson, Quiz, Question, User
from app.schemas.content import LessonOut, CourseOut, QuestionAdminOut

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/users", response_model=list[dict])
def list_users(db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    users = db.query(User).all()
    return [
        {
            "id": u.id, "full_name": u.full_name, "email": u.email,
            "is_admin": u.is_admin, "is_active": u.is_active,
            "created_at": u.created_at,
        }
        for u in users
    ]


@router.patch("/users/{user_id}/toggle-active")
def toggle_user_active(user_id: int, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = not user.is_active
    db.commit()
    return {"id": user.id, "is_active": user.is_active}


@router.post("/courses", response_model=CourseOut, status_code=201)
def create_course(slug: str, title: str, description: str = "", order_index: int = 0,
                   db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    if db.query(Course).filter(Course.slug == slug).first():
        raise HTTPException(status_code=400, detail="Course slug already exists")
    course = Course(slug=slug, title=title, description=description, order_index=order_index)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@router.post("/lessons", response_model=LessonOut, status_code=201)
def create_lesson(
    course_id: int, slug: str, title: str, explanation: str, examples: str,
    practice: str, mini_project: str, order_index: int = 0, level: str = "beginner",
    db: Session = Depends(get_db), admin: User = Depends(get_current_admin),
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    lesson = Lesson(
        course_id=course_id, slug=slug, title=title, order_index=order_index, level=level,
        explanation=explanation, examples=examples, practice=practice, mini_project=mini_project,
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson


@router.delete("/lessons/{lesson_id}", status_code=204)
def delete_lesson(lesson_id: int, db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    db.delete(lesson)
    db.commit()
    return None


@router.post("/quizzes", status_code=201)
def create_quiz(lesson_id: int, title: str = "Lesson Quiz", passing_score: int = 70,
                 db: Session = Depends(get_db), admin: User = Depends(get_current_admin)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    quiz = Quiz(lesson_id=lesson_id, title=title, passing_score=passing_score)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return {"id": quiz.id, "lesson_id": quiz.lesson_id, "title": quiz.title}


@router.post("/questions", status_code=201)
def create_question(
    quiz_id: int, text: str, option_a: str, option_b: str, option_c: str, option_d: str,
    correct_option: str, explanation: str = "",
    db: Session = Depends(get_db), admin: User = Depends(get_current_admin),
):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
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
    return QuestionAdminOut.model_validate(question)
