"""
Kabiru AI Tutor — Database Seed Script.

Populates the database with all 7 courses and 80 real lessons (each with a
quiz), idempotently — safe to run multiple times without creating duplicates.

Run from the backend/ folder with:
    python -m app.seed.run_seed
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from app.core.database import Base, engine, SessionLocal
from app.models.models import Course, Lesson, Quiz, Question

from app.seed.data_python_part1 import PYTHON_LESSONS_PART1
from app.seed.data_python_part2 import PYTHON_LESSONS_PART2
from app.seed.data_python_part3 import PYTHON_LESSONS_PART3
from app.seed.data_python_part4 import PYTHON_LESSONS_PART4
from app.seed.data_python_part5 import PYTHON_LESSONS_PART5
from app.seed.data_python_part6 import PYTHON_LESSONS_PART6
from app.seed.data_sqlite_part1 import SQLITE_LESSONS_PART1
from app.seed.data_sqlite_part2 import SQLITE_LESSONS_PART2
from app.seed.data_fastapi_part1 import FASTAPI_LESSONS_PART1
from app.seed.data_fastapi_part2 import FASTAPI_LESSONS_PART2
from app.seed.data_fastapi_part3 import FASTAPI_LESSONS_PART3
from app.seed.data_linux_part1 import LINUX_LESSONS_PART1
from app.seed.data_linux_part2 import LINUX_LESSONS_PART2
from app.seed.data_git import GIT_LESSONS
from app.seed.data_webdev_part1 import WEBDEV_LESSONS_PART1
from app.seed.data_electronics_part1 import ELECTRONICS_LESSONS_PART1
from app.seed.data_electronics_part2 import ELECTRONICS_LESSONS_PART2
from app.seed.data_electrical_engineering import ELECTRICAL_ENGINEERING_LESSONS


COURSES = [
    {
        "slug": "python",
        "title": "Python Programming",
        "description": (
            "Learn Python from absolute beginner to advanced: variables, data structures, functions, "
            "OOP, error handling, file I/O, decorators, generators, testing, and a final CLI capstone "
            "project. 30 lessons."
        ),
        "order_index": 1,
        "lessons": (
            PYTHON_LESSONS_PART1 + PYTHON_LESSONS_PART2 + PYTHON_LESSONS_PART3
            + PYTHON_LESSONS_PART4 + PYTHON_LESSONS_PART5 + PYTHON_LESSONS_PART6
        ),
    },
    {
        "slug": "sqlite",
        "title": "SQLite Databases",
        "description": (
            "Learn relational databases with SQLite: tables, CRUD operations, filtering, aggregates, "
            "joins, indexes, and safe transactions in Python. 10 lessons."
        ),
        "order_index": 2,
        "lessons": SQLITE_LESSONS_PART1 + SQLITE_LESSONS_PART2,
    },
    {
        "slug": "fastapi",
        "title": "FastAPI Web Development",
        "description": (
            "Build real backend APIs with FastAPI: routing, Pydantic models, database integration, "
            "JWT authentication, middleware, error handling, file uploads, testing, and deployment. "
            "15 lessons."
        ),
        "order_index": 3,
        "lessons": FASTAPI_LESSONS_PART1 + FASTAPI_LESSONS_PART2 + FASTAPI_LESSONS_PART3,
    },
    {
        "slug": "linux",
        "title": "Linux Fundamentals",
        "description": (
            "Master the Linux command line: navigation, file operations, permissions, package "
            "management, process management, and shell scripting. 10 lessons."
        ),
        "order_index": 4,
        "lessons": LINUX_LESSONS_PART1 + LINUX_LESSONS_PART2,
    },
    {
        "slug": "git",
        "title": "Git & GitHub",
        "description": (
            "Learn version control with Git and collaboration on GitHub: commits, branching, merging, "
            "remotes, pull requests, and resolving conflicts. 5 lessons."
        ),
        "order_index": 5,
        "lessons": GIT_LESSONS,
    },
    {
        "slug": "web-development",
        "title": "Web Development Fundamentals",
        "description": (
            "A complete, professional web development curriculum from beginner to expert: HTML, CSS, "
            "JavaScript, modern tooling, React, full-stack integration, performance, security, and a "
            "professional capstone. Built to a Coursera/Udemy-level of depth — lessons are added "
            "progressively; check back as the full 77-lesson curriculum is completed."
        ),
        "order_index": 6,
        "lessons": WEBDEV_LESSONS_PART1,
    },
    {
        "slug": "ai-fundamentals",
        "title": "AI Fundamentals",
        "description": (
            "An introduction to how AI and machine learning work conceptually, and how tools like "
            "Ollama and local language models can be used to build offline-first AI applications like "
            "this tutor."
        ),
        "order_index": 7,
        "lessons": [],
    },
    {
        "slug": "electronics-arduino",
        "title": "Electronics & Arduino/ESP32 Fundamentals",
        "description": (
            "Learn hardware engineering from the ground up: voltage/current/Ohm's Law, core "
            "components, breadboarding, digital and analog I/O on Arduino, sensors, communication "
            "protocols (UART/I2C/SPI), and ESP32 WiFi/IoT, finishing with a capstone IoT dashboard "
            "project. 10 lessons."
        ),
        "order_index": 8,
        "lessons": ELECTRONICS_LESSONS_PART1 + ELECTRONICS_LESSONS_PART2,
    },
    {
        "slug": "electrical-engineering",
        "title": "Electrical Engineering",
        "description": (
            "Learn core electrical engineering: DC and AC circuits, transformers, motors, "
            "generators, inverters, UPS systems, solar power systems, battery management, and "
            "power distribution & protection. 10 lessons."
        ),
        "order_index": 9,
        "lessons": ELECTRICAL_ENGINEERING_LESSONS,
    },
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        total_lessons_created = 0
        total_lessons_updated = 0
        total_quizzes_created = 0
        total_quizzes_updated = 0
        total_questions_created = 0

        for course_data in COURSES:
            course = db.query(Course).filter(Course.slug == course_data["slug"]).first()
            if not course:
                course = Course(
                    slug=course_data["slug"],
                    title=course_data["title"],
                    description=course_data["description"],
                    order_index=course_data["order_index"],
                )
                db.add(course)
                db.commit()
                db.refresh(course)
                print(f"Created course: {course.title}")
            else:
                # Keep description/title in sync if changed, without duplicating the row.
                course.title = course_data["title"]
                course.description = course_data["description"]
                course.order_index = course_data["order_index"]
                db.commit()
                print(f"Course already exists, updated metadata: {course.title}")

            for index, lesson_data in enumerate(course_data["lessons"], start=1):
                lesson = (
                    db.query(Lesson)
                    .filter(Lesson.course_id == course.id, Lesson.slug == lesson_data["slug"])
                    .first()
                )

                lesson_fields = dict(
                    course_id=course.id,
                    slug=lesson_data["slug"],
                    title=lesson_data["title"],
                    order_index=index,
                    level=lesson_data["level"],
                    explanation=lesson_data["explanation"],
                    examples=lesson_data["examples"],
                    practice=lesson_data["practice"],
                    mini_project=lesson_data["mini_project"],
                    # Professional curriculum fields — .get() with "" default so
                    # lessons written before a schema extension still seed fine.
                    real_world_project=lesson_data.get("real_world_project", ""),
                    common_mistakes=lesson_data.get("common_mistakes", ""),
                    best_practices=lesson_data.get("best_practices", ""),
                    interview_questions=lesson_data.get("interview_questions", ""),
                    # Master Directive fields (full 14-part lesson structure).
                    assignment=lesson_data.get("assignment", ""),
                    challenge=lesson_data.get("challenge", ""),
                    summary=lesson_data.get("summary", ""),
                    lesson_references=lesson_data.get("lesson_references", ""),
                    next_lesson_preview=lesson_data.get("next_lesson_preview", ""),
                )

                if lesson:
                    # UPSERT: sync existing row with the latest content instead of
                    # skipping, so edits to lesson data are reflected on re-seed.
                    for field, value in lesson_fields.items():
                        setattr(lesson, field, value)
                    db.commit()
                    total_lessons_updated += 1
                else:
                    lesson = Lesson(**lesson_fields)
                    db.add(lesson)
                    db.commit()
                    db.refresh(lesson)
                    total_lessons_created += 1

                quiz_data = lesson_data.get("quiz")
                if quiz_data:
                    quiz = db.query(Quiz).filter(Quiz.lesson_id == lesson.id).first()
                    if quiz:
                        quiz.title = quiz_data["title"]
                        quiz.passing_score = quiz_data["passing_score"]
                        # Replace questions wholesale so edits/removals in code
                        # are reflected, rather than accumulating stale rows.
                        db.query(Question).filter(Question.quiz_id == quiz.id).delete()
                        db.commit()
                        total_quizzes_updated += 1
                    else:
                        quiz = Quiz(
                            lesson_id=lesson.id,
                            title=quiz_data["title"],
                            passing_score=quiz_data["passing_score"],
                        )
                        db.add(quiz)
                        db.commit()
                        db.refresh(quiz)
                        total_quizzes_created += 1

                    for q in quiz_data["questions"]:
                        question = Question(
                            quiz_id=quiz.id,
                            text=q["text"],
                            option_a=q["option_a"],
                            option_b=q["option_b"],
                            option_c=q["option_c"],
                            option_d=q["option_d"],
                            correct_option=q["correct_option"],
                            explanation=q["explanation"],
                        )
                        db.add(question)
                        total_questions_created += 1
                    db.commit()

        print("\nSeeding complete.")
        print(f"  New lessons created:     {total_lessons_created}")
        print(f"  Existing lessons synced: {total_lessons_updated}")
        print(f"  New quizzes created:     {total_quizzes_created}")
        print(f"  Existing quizzes synced: {total_quizzes_updated}")
        print(f"  Questions written:       {total_questions_created}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
