"""
Kabiru AI Tutor - FastAPI application entrypoint.

Run with:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.database import Base, engine
from app.core.rate_limit import check_general_rate_limit
from app.models import models  # noqa: F401  (ensures models are registered before create_all)

from app.routers import auth, courses, lessons, quizzes, progress, notes, certificates, chat, admin

# Create all tables on startup if they don't exist yet (SQLite-friendly).
# For production schema evolution, use Alembic migrations instead (see /backend/alembic).
Base.metadata.create_all(bind=engine)

# Uploads directory (profile photos, etc.) — created here so a fresh clone
# or first deploy never 500s on a missing directory. See UPLOAD_DIR in
# core/config.py for the production-persistence caveat.
AVATAR_UPLOAD_DIR = os.path.join(settings.UPLOAD_DIR, "avatars")
os.makedirs(AVATAR_UPLOAD_DIR, exist_ok=True)

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


@app.middleware("http")
async def general_rate_limit_middleware(request: Request, call_next):
    """Per-IP request-volume limiter for every endpoint (see core/rate_limit.py).
    Auth endpoints still get their own tighter, identifier-based limiter on
    top of this — this one is a coarse, app-wide backstop."""
    if settings.GENERAL_RATE_LIMIT_ENABLED:
        try:
            check_general_rate_limit(request)
        except Exception as exc:
            status_code = getattr(exc, "status_code", 429)
            detail = getattr(exc, "detail", "Too many requests.")
            headers = getattr(exc, "headers", None) or {}
            return JSONResponse(status_code=status_code, content={"detail": detail}, headers=headers)
    return await call_next(request)


# Serves uploaded profile photos at /uploads/avatars/<filename>, matching
# User.avatar_url in models.py.
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

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
