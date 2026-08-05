"""
Kabiru AI Tutor - FastAPI application entrypoint.

Run with:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import Base, engine
from app.models import models  # noqa: F401  (ensures models are registered before create_all)

from app.routers import auth, courses, lessons, quizzes, progress, notes, certificates, chat, admin

# Create all tables on startup if they don't exist yet (SQLite-friendly).
# For production schema evolution, use Alembic migrations instead (see /backend/alembic).
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Offline-first AI tutoring platform teaching Python, SQLite, FastAPI, Linux, Git, Web Dev, and AI Fundamentals.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(lessons.router)
app.include_router(quizzes.router)
app.include_router(progress.router)
app.include_router(notes.router)
app.include_router(certificates.router)
app.include_router(chat.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "status": "running",
        "docs": "/docs",
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.ENV,
        # Non-sensitive diagnostic flag: helps confirm at a glance whether this
        # deployment is at risk of losing data on redeploy (see docs/PRODUCTION_FIXES.md).
        "database_persistent": not settings.using_sqlite,
    }
