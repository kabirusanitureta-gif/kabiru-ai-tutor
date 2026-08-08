"""
Short-lived server-side storage for WebAuthn (Face ID / Touch ID / Windows
Hello) registration and login challenges.

Same in-memory, single-process pattern as core/rate_limit.py — no new
dependency (no Redis), fine for a single worker/instance. A WebAuthn
challenge only needs to live for the ~1-2 minutes between "show the
biometric prompt" and "verify what it returned", so the entries here are
opportunistically expired rather than needing a background sweeper.

LIMITATION (documented, not hidden): if you scale to multiple
workers/instances, a challenge created on one process won't be visible to
another, so an in-flight registration/login could fail with "state not
found" if the second request lands on a different worker. At that point,
move this to a shared store (e.g. Redis) — callers in routers/webauthn.py
won't need to change, only this file.
"""
import time
import uuid
from threading import Lock
from typing import Optional

_CHALLENGE_TTL_SECONDS = 120

# state_id -> {"challenge": bytes, "user_id": int | None, "email": str | None, "expires": float}
_states: dict[str, dict] = {}
_lock = Lock()


def _prune_expired() -> None:
    now = time.time()
    expired = [k for k, v in _states.items() if v["expires"] < now]
    for k in expired:
        _states.pop(k, None)


def save_challenge(challenge: bytes, user_id: Optional[int] = None, email: Optional[str] = None) -> str:
    """Store a challenge for the duration of one registration/login round
    trip and return an opaque state_id the client must echo back on verify."""
    state_id = uuid.uuid4().hex
    with _lock:
        _prune_expired()
        _states[state_id] = {
            "challenge": challenge,
            "user_id": user_id,
            "email": email,
            "expires": time.time() + _CHALLENGE_TTL_SECONDS,
        }
    return state_id


def pop_challenge(state_id: str) -> Optional[dict]:
    """Retrieve and immediately delete a stored challenge (single use, like
    a nonce should be) — returns None if it never existed, already expired,
    or was already consumed."""
    with _lock:
        _prune_expired()
        return _states.pop(state_id, None)
