"""
Password hashing and JWT token creation / verification.
"""
import hashlib
import secrets
from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None


# ---------------------------------------------------------------------------
# Refresh tokens & password-reset codes
#
# These are opaque random strings, NOT JWTs. Only a SHA-256 hash of them is
# ever stored in the database (see RefreshToken / PasswordResetToken models),
# so a database leak alone can't be replayed as a valid token — same
# principle as password hashing, just with a fast hash since these are
# already high-entropy random values (no need for bcrypt's slow KDF here).
# ---------------------------------------------------------------------------

def generate_refresh_token() -> str:
    """Cryptographically random, URL-safe opaque refresh token (plaintext, given to client once)."""
    return secrets.token_urlsafe(48)


def hash_token(token: str) -> str:
    """SHA-256 hex digest, used to look up / store refresh & reset tokens without keeping plaintext."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def generate_reset_code() -> str:
    """6-digit numeric password-reset code (easy for a user to read/type from an email)."""
    return f"{secrets.randbelow(1_000_000):06d}"
