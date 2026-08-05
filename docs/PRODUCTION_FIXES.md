# Production Fixes — Root Causes and Solutions

This document explains the real root causes behind three production issues that came up after
deploying Kabiru AI Tutor, and exactly what was changed to fix them permanently.

---

## 1. "Incorrect email or password" and JWT failures after redeploy

**This was never an authentication bug.** Password hashing, JWT creation, and JWT verification were
all working correctly the whole time (confirmed by live testing against the Render deployment).

**Root cause:** Render's (and Railway's) free web services run on an **ephemeral filesystem**. Every
redeploy — and even periodic restarts on the free tier — wipes any files written to local disk,
including the SQLite database file (`kabiru_tutor.db`). `run_seed.py` re-creates the *lesson content*
(courses/lessons/quizzes) because that data lives in the codebase and re-seeding is idempotent — but
**registered users are gone**, because they were never part of the seed data; they only ever existed
in that now-deleted SQLite file.

So after a redeploy:
- Old users can't log in → looks like "incorrect password" (the user record simply doesn't exist)
- Old JWTs become meaningless → `get_current_user` looks up the user by ID and finds nothing →
  "Could not validate credentials"

### The fix

Switch `DATABASE_URL` from SQLite to a **persistent Postgres** database in production. This was
implemented in three places:

- `backend/app/core/database.py` — now detects Postgres URLs, normalizes Render's `postgres://` prefix
  to the `postgresql://` SQLAlchemy requires, and adds `pool_pre_ping` + `pool_recycle` so idle
  connections on free-tier Postgres don't cause silent failures.
- `requirements.txt` — added `psycopg2-binary` (the Postgres driver).
- `render.yaml` — provisions a **free managed Postgres database** automatically and wires its
  connection string into the backend service's `DATABASE_URL` — no manual copy-pasting required.

**If you already have a Render backend deployed with SQLite:** redeploying with the new `render.yaml`
Blueprint (see below) will provision Postgres for you. Any users registered under the old SQLite setup
are already lost (they were wiped on every restart anyway) — everyone will need to register again
once, and from that point on their accounts will persist across all future redeploys.

---

## 2. Vite/esbuild segmentation fault in Termux

**Root cause:** This is a known upstream compatibility issue between esbuild's compiled Go binary and
Termux's `bionic` libc on Android. It is not something fixable from application code — esbuild simply
crashes when its native binary runs under Termux's non-glibc environment for certain build operations.

### The fix

**Don't build the frontend on-device in Termux at all.** Instead, let a real Linux build server do it:

- **`render.yaml`** now defines the frontend as a Render **Static Site**, which builds
  (`npm ci && npm run build`) on Render's own Linux infrastructure and serves the static output —
  Termux is never involved.
- **`frontend/vercel.json`** provides the equivalent one-click configuration for deploying to Vercel
  instead, if you prefer — same idea: Vercel's servers build it, your phone never runs esbuild.

You can still use Termux for **local development** (`npm run dev`, which uses Vite's dev server and
generally does not trigger the same crash), just not for the production `build` step.

---

## 3. Frontend/backend production configuration

Several smaller fixes round out production-readiness:

- **CORS now supports multiple origins.** `FRONTEND_ORIGIN` in `.env` can be a comma-separated list
  (`backend/app/core/config.py` → `frontend_origins` property), so you can allow your Render static
  site URL, a Vercel URL, and a custom domain simultaneously without editing code.
- **`SECRET_KEY` production check.** If `ENV=production` and `SECRET_KEY` is still the insecure default,
  the backend now logs a loud warning on startup. `render.yaml` sets `generateValue: true` so Render
  generates a strong random secret automatically — you never have to think about it.
- **Certificate downloads are now self-healing.** Certificate *records* live in the database
  (persistent once on Postgres), but the generated PDF *files* still live on local disk, which can
  still be wiped by a restart even with Postgres for the DB. `backend/app/routers/certificates.py` now
  detects a missing PDF file and regenerates it on-demand from the stored certificate code, so a
  student never gets an unexpected 404 for a certificate they already earned.
- **`VITE_API_URL` build-time reminder.** Vite environment variables are baked in at *build* time, not
  runtime — `frontend/.env.production.example` documents this explicitly so the variable is set in the
  right place (your hosting platform's build environment, not just a local `.env` file).

---

## Deploying with the new setup

### Render (recommended — one Blueprint deploys everything)

1. Push these changes to GitHub.
2. Go to [dashboard.render.com/blueprints](https://dashboard.render.com/blueprints) → **New Blueprint
   Instance** → select this repository. Render reads `render.yaml` and creates the Postgres database,
   backend web service, and frontend static site automatically, with all environment variables wired
   correctly.
3. Once deployed, register a fresh account (previous SQLite-based accounts were already lost to the
   ephemeral disk issue) and confirm login survives a manual redeploy — trigger one from the Render
   dashboard and log in again afterward to verify.

### Vercel (frontend only, if you prefer it over Render's static site)

1. Import the repository into Vercel, set the project's root directory to `frontend`.
2. Vercel auto-detects `frontend/vercel.json`.
3. Add the environment variable `VITE_API_URL` pointing at your backend's URL, in the **Build & Development
   Settings**, before deploying.

### Manual (Railway or otherwise)

If configuring by hand instead of using `render.yaml`, the two settings that caused the earlier Railway
issues are worth double-checking explicitly:
- **Root Directory** must point at `backend` or `frontend` respectively (not the repo root, not the
  path with a leading `/`).
- **Start Command** for the backend service must not include `cd backend` if Root Directory is already
  `backend` — otherwise it tries to `cd` into a nonexistent `backend/backend`.
