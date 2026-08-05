import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.models import Quiz, Question, Attempt, Progress, Lesson, User
from app.schemas.content import QuizOut, QuizSubmit, AttemptOut
from app.services.lesson_lock import assert_lesson_unlocked

router = APIRouter(prefix="/api/quizzes", tags=["quizzes"])


def _assert_quiz_lesson_unlocked(db: Session, current_user: User, quiz: Quiz) -> None:
    lesson = db.query(Lesson).filter(Lesson.id == quiz.lesson_id).first()
    if lesson:
        assert_lesson_unlocked(db, current_user, lesson)


@router.get("/lesson/{lesson_id}", response_model=list[QuizOut])
def get_quizzes_for_lesson(lesson_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    assert_lesson_unlocked(db, current_user, lesson)
    quizzes = db.query(Quiz).filter(Quiz.lesson_id == lesson_id).all()
    return quizzes


@router.get("/{quiz_id}", response_model=QuizOut)
def get_quiz(quiz_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    _assert_quiz_lesson_unlocked(db, current_user, quiz)
    return quiz


@router.post("/{quiz_id}/submit", response_model=AttemptOut)
def submit_quiz(quiz_id: int, payload: QuizSubmit, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    _assert_quiz_lesson_unlocked(db, current_user, quiz)

    questions = db.query(Question).filter(Question.quiz_id == quiz_id).all()
    if not questions:
        raise HTTPException(status_code=400, detail="Quiz has no questions")

    correct_count = 0
    for question in questions:
        student_answer = payload.answers.get(question.id)
        if student_answer and student_answer.lower() == question.correct_option.lower():
            correct_count += 1

    score_percent = round((correct_count / len(questions)) * 100, 2)
    passed = score_percent >= quiz.passing_score

    attempt = Attempt(
        user_id=current_user.id,
        quiz_id=quiz_id,
        score_percent=score_percent,
        passed=passed,
        answers_json=json.dumps({str(k): v for k, v in payload.answers.items()}),
    )
    db.add(attempt)

    if passed:
        progress = (
            db.query(Progress)
            .filter(Progress.user_id == current_user.id, Progress.lesson_id == quiz.lesson_id)
            .first()
        )
        if not progress:
            progress = Progress(user_id=current_user.id, lesson_id=quiz.lesson_id)
            db.add(progress)
        progress.quiz_passed = True

    db.commit()
    db.refresh(attempt)
    return attempt


@router.get("/attempts/mine", response_model=list[AttemptOut])
def my_attempts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return (
        db.query(Attempt)
        .filter(Attempt.user_id == current_user.id)
        .order_by(Attempt.created_at.desc())
        .limit(50)
        .all()
    )
