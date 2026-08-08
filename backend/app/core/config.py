"""
Application configuration, loaded from environment variables / .env file.
"""
import os
import logging
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger("kabiru.config")

INSECURE_DEFAULT_SECRET = "insecure-dev-key-change-me"


class Settings(BaseSettings):
    APP_NAME: str = "Kabiru AI Tutor"
    ENV: str = "development"  # set to "production" on Render/Railway/Vercel

    SECRET_KEY: str = INSECURE_DEFAULT_SECRET
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # --- Refresh tokens ---
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # --- Forgot / reset password ---
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 15

    # --- Email verification (registration PIN) ---
    EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES: int = 15

    # --- Login rate limiting / brute-force protection ---
    # In-memory (per-process) sliding window. Fine for a single Render
    # instance/worker; if you scale to multiple workers or instances, move
    # this to a shared store (e.g. Redis) since counters won't be shared.
    LOGIN_RATE_LIMIT_ATTEMPTS: int = 5
    LOGIN_RATE_LIMIT_WINDOW_MINUTES: int = 15

    # --- General request rate limiting (all endpoints, not just auth) ---
    # Same in-memory per-process sliding window as the login limiter, applied
    # to every request by IP. Generous default so normal app usage (a page
    # doing several API calls at once) never trips it.
    GENERAL_RATE_LIMIT_ENABLED: bool = True
    GENERAL_RATE_LIMIT_REQUESTS: int = 120
    GENERAL_RATE_LIMIT_WINDOW_SECONDS: int = 60

    # --- Profile photo uploads ---
    AVATAR_MAX_SIZE_MB: int = 2
    AVATAR_ALLOWED_CONTENT_TYPES: str = "image/jpeg,image/png,image/webp"
    # Relative to the backend working directory. On Render/Railway free
    # tiers this filesystem is ephemeral (same caveat as SQLite, see
    # DATABASE_URL below) — uploaded avatars will be lost on redeploy unless
    # you mount a persistent disk or switch to object storage (S3-compatible).
    UPLOAD_DIR: str = "uploads"

    # --- Outgoing email (forgot-password codes) ---
    # Optional: if SMTP_HOST is blank, emails are just logged instead of sent
    # (safe no-op default so this never breaks deploys that haven't set up
    # email yet). Set all SMTP_* vars to actually deliver reset codes.
    SMTP_HOST: str = ""
    SMTP_PORT: int = 465
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "no-reply@kabiru-ai-tutor.local"
    SMTP_USE_TLS: bool = False

    # SQLite by default for local/offline use (Termux/Pydroid/Linux/Windows).
    # In production (Render/Railway), set this to a Postgres URL so data
    # survives redeploys — see docs/PRODUCTION_FIXES.md for why this matters.
    DATABASE_URL: str = "sqlite:///./kabiru_tutor.db"

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    # Explicit override: if set and actually installed in Ollama, this exact
    # model is used regardless of the priority list below. Leave as the
    # default "auto" to let the backend auto-detect the best installed model.
    OLLAMA_MODEL: str = "auto"
    OLLAMA_ENABLED: bool = True
    # Priority order used when OLLAMA_MODEL="auto": the backend lists every
    # model actually installed in the local Ollama instance and picks the
    # first one whose name contains one of these family names, in this order.
    # Customize via env var, comma-separated, e.g. "llama,qwen,mistral".
    OLLAMA_PREFERRED_MODELS: str = "qwen,deepseek,llama,gemma,mistral"

    # --- Cloud AI fallback: Groq (https://console.groq.com) ---
    # Free, permanent, no-credit-card tier — see docs/AI_PROVIDER.md for why
    # Groq was chosen. Leave AI_API_KEY empty to disable and use the
    # rule-based tutor only (e.g. in CI or fully offline environments).
    AI_API_KEY: str = ""
    AI_API_BASE_URL: str = "https://api.groq.com/openai/v1"
    AI_API_MODEL: str = "llama-3.3-70b-versatile"
    AI_API_TIMEOUT_SECONDS: float = 20.0

    # Comma-separated list of allowed frontend origins, e.g.
    # "https://kabiru-tutor.vercel.app,https://kabiru-tutor.onrender.com"
    # A single origin (no comma) also works fine.
    FRONTEND_ORIGIN: str = "http://localhost:5173"

    # --- WebAuthn (Face ID / Touch ID / Windows Hello / security keys) ---
    # RP_ID must be the bare domain the frontend is served from (no scheme,
    # no port, no path) — e.g. "kabiru-tutor.vercel.app" in production. The
    # default "localhost" only works for local dev. ORIGIN must be the exact
    # scheme+host(+port) the browser shows in its address bar; comma-separate
    # multiple values (e.g. a Vercel preview URL and the production domain)
    # the same way FRONTEND_ORIGIN works above. A mismatch here is the most
    # common cause of "Registration failed" from a real deployment.
    WEBAUTHN_RP_ID: str = "localhost"
    WEBAUTHN_RP_NAME: str = "Kabiru AI Tutor"
    WEBAUTHN_ORIGIN: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def frontend_origins(self) -> list[str]:
        """FRONTEND_ORIGIN parsed into a clean list, supporting comma-separated values."""
        origins = [o.strip() for o in self.FRONTEND_ORIGIN.split(",") if o.strip()]
        # Always allow local dev origins too, so local frontend testing never breaks
        # even when FRONTEND_ORIGIN is set to a production URL.
        for local in ("http://localhost:5173", "http://127.0.0.1:5173"):
            if local not in origins:
                origins.append(local)
        return origins

    @property
    def ollama_preferred_models_list(self) -> list[str]:
        """OLLAMA_PREFERRED_MODELS parsed into a clean, lowercase priority list."""
        return [m.strip().lower() for m in self.OLLAMA_PREFERRED_MODELS.split(",") if m.strip()]

    @property
    def is_production(self) -> bool:
        return self.ENV.lower() == "production"

    @property
    def using_sqlite(self) -> bool:
        return self.DATABASE_URL.startswith("sqlite")

    @property
    def email_configured(self) -> bool:
        return bool(self.SMTP_HOST and self.SMTP_USER and self.SMTP_PASSWORD)

    @property
    def avatar_allowed_content_types_list(self) -> list[str]:
        return [t.strip().lower() for t in self.AVATAR_ALLOWED_CONTENT_TYPES.split(",") if t.strip()]

    @property
    def webauthn_origins_list(self) -> list[str]:
        """WEBAUTHN_ORIGIN parsed into a clean list, same comma-separated
        convention as frontend_origins. A registration/login is only
        accepted if the browser's reported origin is one of these.
        Localhost dev origins are only auto-added outside production —
        a production deployment should never silently accept a passkey
        registered from someone's local dev machine."""
        origins = [o.strip() for o in self.WEBAUTHN_ORIGIN.split(",") if o.strip()]
        if not self.is_production:
            for local in ("http://localhost:5173", "http://127.0.0.1:5173"):
                if local not in origins:
                    origins.append(local)
        return origins


@lru_cache
def get_settings() -> Settings:
    s = Settings()

    # Loud, impossible-to-miss warnings for the two most common production
    # misconfigurations that caused real outages in this project:
    if s.is_production and s.SECRET_KEY == INSECURE_DEFAULT_SECRET:
        logger.warning(
            "SECURITY WARNING: SECRET_KEY is still the insecure default value. "
            "Set a unique SECRET_KEY environment variable in your hosting dashboard "
            "(Render/Railway/Vercel). Generate one with: "
            "python -c \"import secrets; print(secrets.token_hex(32))\""
        )
    if s.is_production and s.using_sqlite:
        logger.warning(
            "PERSISTENCE WARNING: DATABASE_URL is still SQLite in production. "
            "On Render/Railway, the local filesystem is ephemeral and is wiped on "
            "every redeploy or restart — this WILL cause registered users and their "
            "progress to disappear (symptoms: 'Incorrect email or password' and JWT "
            "validation failures after a redeploy, even with correct credentials). "
            "Set DATABASE_URL to a persistent Postgres connection string instead. "
            "See docs/PRODUCTION_FIXES.md."
        )
    if s.is_production:
        logger.warning(
            "UPLOAD WARNING: profile photos are stored on local disk under "
            "UPLOAD_DIR, which is ephemeral on Render/Railway free tiers just "
            "like SQLite — uploaded avatars will disappear on redeploy. For "
            "durable storage in production, mount a persistent disk or move "
            "avatar storage to S3-compatible object storage."
        )
    if s.is_production and s.WEBAUTHN_RP_ID == "localhost":
        logger.warning(
            "WEBAUTHN WARNING: WEBAUTHN_RP_ID is still 'localhost'. Set it to your "
            "production frontend's bare domain (e.g. 'kabiru-tutor.vercel.app') and "
            "set WEBAUTHN_ORIGIN to the exact URL(s) users load the app from, or "
            "Face ID / Touch ID / passkey registration and login will fail there."
        )
    if s.is_production and not s.email_configured:
        logger.warning(
            "EMAIL WARNING: SMTP_HOST/SMTP_USER/SMTP_PASSWORD are not set. "
            "Forgot-password codes will be logged on the server instead of "
            "emailed to users. Set the SMTP_* environment variables to enable "
            "real delivery."
        )

    return s


settings = get_settings()
