"""
SQLAlchemy engine, session factory, and declarative base.

Supports two modes:
- SQLite (default): zero-setup, works offline on Termux/Pydroid/Linux/Windows.
  NOT suitable for Render/Railway production — their filesystems are
  ephemeral and wipe the .db file on every redeploy/restart.
- Postgres: set DATABASE_URL to a postgresql:// connection string for
  production deployments where data must survive redeploys.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings

connect_args = {}
engine_kwargs = {"echo": False}

if settings.using_sqlite:
    # check_same_thread=False is required because FastAPI may use the
    # session across threads within a single request lifecycle.
    connect_args = {"check_same_thread": False}
else:
    # Postgres (and other server-based DBs): verify connections are alive
    # before use. This prevents "SSL connection has been closed unexpectedly"
    # errors after the DB server closes idle connections, which is common on
    # free-tier hosted Postgres instances.
    engine_kwargs["pool_pre_ping"] = True
    engine_kwargs["pool_recycle"] = 300

# Render's managed Postgres gives URLs starting with "postgres://", but
# SQLAlchemy 2.x requires the "postgresql://" scheme. Normalize it so
# copy-pasting Render's connection string just works.
database_url = settings.DATABASE_URL
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

if not settings.using_sqlite and "sslmode" not in database_url and "localhost" not in database_url:
    # Most hosted Postgres providers (Render, Railway, Supabase, etc.) require
    # SSL for external connections. Adding it defensively here prevents a
    # class of opaque connection failures on first deploy, without requiring
    # every DATABASE_URL to remember to include it manually.
    separator = "&" if "?" in database_url else "?"
    database_url = f"{database_url}{separator}sslmode=require"

engine = create_engine(database_url, connect_args=connect_args, **engine_kwargs)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
