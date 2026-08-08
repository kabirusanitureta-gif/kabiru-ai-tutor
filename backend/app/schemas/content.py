from datetime import datetime
from pydantic import BaseModel


class LessonOut(BaseModel):
    id: int
    course_id: int
    slug: str
    title: str
    order_index: int
    level: str
    explanation: str
    examples: str
    practice: str
    mini_project: str
    real_world_project: str = ""
    common_mistakes: str = ""
    best_practices: str = ""
    interview_questions: str = ""
    assignment: str = ""
    challenge: str = ""
    summary: str = ""
    lesson_references: str = ""
    next_lesson_preview: str = ""
    is_completed: bool = False

    class Config:
        from_attributes = True


class LessonSummary(BaseModel):
    id: int
    slug: str
    title: str
    order_index: int
    level: str
    locked: bool = False

    class Config:
        from_attributes = True


class CourseOut(BaseModel):
    id: int
    slug: str
    title: str
    description: str
    order_index: int
    lessons: list[LessonSummary] = []

    class Config:
        from_attributes = True


class QuestionOut(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str

    class Config:
        from_attributes = True


class QuestionAdminOut(QuestionOut):
    correct_option: str
    explanation: str


class QuizOut(BaseModel):
    id: int
    lesson_id: int
    title: str
    passing_score: int
    questions: list[QuestionOut] = []
    quiz_passed: bool = False
    best_score_percent: float | None = None

    class Config:
        from_attributes = True


class QuizSubmit(BaseModel):
    answers: dict[int, str]  # question_id -> 'a'|'b'|'c'|'d'


class AttemptOut(BaseModel):
    id: int
    quiz_id: int
    score_percent: float
    passed: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ProgressOut(BaseModel):
    lesson_id: int
    completed: bool
    quiz_passed: bool
    completed_at: datetime | None

    class Config:
        from_attributes = True


class NoteCreate(BaseModel):
    title: str = "Untitled note"
    content: str = ""
    lesson_id: int | None = None


class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    lesson_id: int | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CertificateOut(BaseModel):
    id: int
    course_id: int
    certificate_code: str
    issued_at: datetime

    class Config:
        from_attributes = True


class ChatIn(BaseModel):
    message: str


class ChatOut(BaseModel):
    reply: str
    language: str


class CodeCheckIn(BaseModel):
    code: str
    language: str = "python"
    task_description: str = ""


class CodeCheckOut(BaseModel):
    passed_basic_checks: bool
    feedback_en: str
    feedback_ha: str
    errors: list[str] = []
