"""
Lightweight brute-force protection for auth endpoints.

This is an in-memory, per-process sliding-window limiter keyed by
(client IP, identifier e.g. email). No new dependency (no Redis, no
slowapi) so it works everywhere this project already runs, including
plain SQLite/offline mode.

LIMITATION (documented, not hidden): counters live in this process's
memory only. That's correct for a single Render web-service instance
running a single worker (this project's default `uvicorn` start
command). If you later scale to multiple workers/instances, each
process gets its own counters, so the effective limit multiplies by
the number of processes. At that point, swap this for a Redis-backed
limiter — the call sites in auth.py won't need to change, only this
file.
"""
import time
from collections import defaultdict
from threading import Lock

from fastapi import HTTPException, Request, status

from app.core.config import settings

# key -> list[timestamps] of recent failed/attempted actions
_attempts: dict[str, list[float]] = defaultdict(list)
_lock = Lock()


def _client_ip(request: Request) -> str:
    # Render/most PaaS put the real client IP in X-Forwarded-For.
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def check_rate_limit(request: Request, identifier: str, scope: str) -> None:
    """
    Raise 429 if `identifier` (e.g. an email) has too many recent attempts
    for `scope` (e.g. "login", "forgot-password"). Call this BEFORE doing
    the expensive/sensitive work (password verification, sending email).
    """
    key = f"{scope}:{_client_ip(request)}:{identifier.lower().strip()}"
    window_seconds = settings.LOGIN_RATE_LIMIT_WINDOW_MINUTES * 60
    limit = settings.LOGIN_RATE_LIMIT_ATTEMPTS
    now = time.time()

    with _lock:
        recent = [t for t in _attempts[key] if now - t < window_seconds]
        _attempts[key] = recent
        if len(recent) >= limit:
            retry_after = int(window_seconds - (now - recent[0]))
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=(
                    f"Too many attempts. Please try again in "
                    f"{max(retry_after // 60, 1)} minute(s)."
                ),
                headers={"Retry-After": str(max(retry_after, 1))},
            )


def record_attempt(request: Request, identifier: str, scope: str) -> None:
    """Record one attempt (call after a failed login / any reset request)."""
    key = f"{scope}:{_client_ip(request)}:{identifier.lower().strip()}"
    with _lock:
        _attempts[key].append(time.time())


def clear_attempts(request: Request, identifier: str, scope: str) -> None:
    """Call after a SUCCESSFUL login to reset the counter for that identifier."""
    key = f"{scope}:{_client_ip(request)}:{identifier.lower().strip()}"
    with _lock:
        _attempts.pop(key, None)


# ---------------------------------------------------------------------------
# General per-IP request rate limiting (all endpoints).
#
# Separate counter store from the auth-specific one above, since this limits
# request *volume* per IP rather than failed *attempts* per identifier — a
# single generous window is enough to blunt basic scraping/DoS without
# affecting normal usage. Same in-memory, single-process limitation applies
# (see module docstring); scale to Redis if you move to multiple workers.
# ---------------------------------------------------------------------------
_general_hits: dict[str, list[float]] = defaultdict(list)
_general_lock = Lock()


def check_general_rate_limit(request: Request) -> None:
    """Raise 429 if this client IP has made too many requests recently, across all endpoints."""
    ip = _client_ip(request)
    window_seconds = settings.GENERAL_RATE_LIMIT_WINDOW_SECONDS
    limit = settings.GENERAL_RATE_LIMIT_REQUESTS
    now = time.time()

    with _general_lock:
        recent = [t for t in _general_hits[ip] if now - t < window_seconds]
        recent.append(now)
        _general_hits[ip] = recent
        if len(recent) > limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many requests. Please slow down and try again shortly.",
                headers={"Retry-After": str(window_seconds)},
            )
