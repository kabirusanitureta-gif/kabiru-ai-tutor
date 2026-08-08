from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator


# Placeholder / template strings that must NEVER be stored as a real user's name.
# This is a defensive backstop — the frontend should never send these, but if a
# stale build, bad autofill, or bug upstream ever does, the API rejects it here
# instead of silently persisting bad data.
_DISALLOWED_NAME_VALUES = {
    "your full name",
    "kabiru sani",
    "full name",
    "enter your name",
    "enter full name",
}


def _clean_full_name(value: str) -> str:
    cleaned = " ".join(value.strip().split())  # trim + collapse internal whitespace
    if not cleaned:
        raise ValueError("Full name cannot be empty.")
    if cleaned.lower() in _DISALLOWED_NAME_VALUES:
        raise ValueError("Please enter your actual full name.")
    return cleaned


class UserCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)
    preferred_language: str = "en"

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, v: str) -> str:
        return _clean_full_name(v)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    preferred_language: str
    theme: str
    is_admin: bool
    created_at: datetime
    # Optional so existing clients that don't read these fields keep working
    # unchanged; new frontend code uses them for the profile photo and RBAC.
    avatar_url: str | None = None
    role: str = "student"
    # Optional so existing clients that don't read this field keep working
    # unchanged; defaults True to match every account created before this
    # field existed (backfilled True by the migration, never asked to verify
    # retroactively). New registrations start False.
    is_verified: bool = True

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
    # Optional so existing clients that don't read this field keep working
    # unchanged; new frontend code uses it to enable silent token refresh.
    refresh_token: str | None = None


class UserUpdate(BaseModel):
    full_name: str | None = None
    preferred_language: str | None = None
    theme: str | None = None

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, v: str | None) -> str | None:
        if v is None:
            return v
        return _clean_full_name(v)


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class LogoutRequest(BaseModel):
    refresh_token: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class VerifyEmailRequest(BaseModel):
    email: EmailStr
    pin: str = Field(min_length=6, max_length=6)


class ResendVerificationRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    code: str = Field(min_length=6, max_length=6)
    new_password: str = Field(min_length=6, max_length=128)


# ---------------------------------------------------------------------------
# WebAuthn (Face ID / Touch ID / Windows Hello / security keys)
# ---------------------------------------------------------------------------

class WebAuthnRegisterVerifyRequest(BaseModel):
    state_id: str
    # Raw JSON the browser's navigator.credentials.create() returned, passed
    # straight through from @simplewebauthn/browser's startRegistration().
    credential: dict
    device_name: str | None = Field(default=None, max_length=120)


class WebAuthnLoginOptionsRequest(BaseModel):
    # Optional: if omitted, this is a "usernameless"/discoverable-credential
    # flow — the authenticator itself (Face ID's account picker, etc.)
    # decides which passkey to offer, so no email round-trip is needed.
    email: EmailStr | None = None


class WebAuthnLoginVerifyRequest(BaseModel):
    state_id: str
    credential: dict


class WebAuthnCredentialOut(BaseModel):
    id: int
    device_name: str | None
    transports: str | None
    created_at: datetime
    last_used_at: datetime | None

    class Config:
        from_attributes = True


class WebAuthnCredentialRename(BaseModel):
    device_name: str = Field(min_length=1, max_length=120)
