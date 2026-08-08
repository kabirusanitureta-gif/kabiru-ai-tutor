# 🎓 Kabiru AI Tutor

A complete, production-ready, **offline-first AI tutoring platform** that teaches programming from
absolute beginner to expert — built for **Kabiru Sani** (Nigeria) and anyone else who wants to learn
to code without depending on an internet connection or paid API.

Kabiru AI Tutor teaches:
- 🐍 **Python** — 30 lessons, variables to a final CLI capstone project
- 🗄️ **SQLite** — 10 lessons on databases, queries, joins, and transactions
- ⚡ **FastAPI** — 15 lessons building real, secured, tested REST APIs
- 🐧 **Linux** — 10 lessons mastering the terminal and shell scripting
- 🔧 **Git & GitHub** — 5 lessons on version control and collaboration

Every lesson includes an **explanation**, **examples**, **practice exercises**, a **mini project**, and
an auto-graded **quiz**. The built-in AI tutor answers questions in **Hausa or English**, checks
student code, explains errors in simple terms, and recommends the next lesson automatically.

---

## ✨ Features

- 🔐 User registration & login (JWT authentication)
- 🆔 Face ID / Touch ID / Windows Hello passwordless login (WebAuthn passkeys) — biometric data
  never leaves the user's device or reaches the server
- 📈 Persistent progress tracking per lesson and per course
- ✅ Auto-graded quizzes with a passing-score threshold
- 💻 Real Python code execution & checking, with bilingual error explanations
- 🧭 Automatic "what should I learn next" recommendation
- 📊 Full progress dashboard with daily study streaks
- 🎓 Auto-issued PDF certificates when a course is fully completed
- 🤖 AI chat tutor — uses a local **Ollama** model if available, otherwise falls back to a built-in
  rule-based tutor so the app **never** requires an internet connection or paid API key
- 📝 Personal notes tied to lessons
- 🔍 Full-text lesson search
- 🌗 Dark / light mode
- 🇳🇬 Hausa + English interface
- 📱 Mobile-first responsive design (works great on a phone browser)

---

## 🧱 Tech Stack

**Backend:** Python 3.12+, FastAPI, SQLAlchemy, SQLite, JWT (python-jose), Alembic, ReportLab (PDF
certificates)

**Frontend:** React 18, Vite, Tailwind CSS, React Router, Axios

**Local AI:** [Ollama](https://ollama.com) — automatically detects and uses the best model you have
installed (priority: Qwen > DeepSeek > Llama > Gemma > Mistral, configurable). If Ollama isn't
installed, the app works fully offline with a built-in rule-based tutor as a fallback.

---

## 📁 Project Structure

```
kabiru-ai-tutor/
├── backend/
│   ├── app/
│   │   ├── core/          # config, database, security, deps
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic request/response schemas
│   │   ├── routers/       # auth, courses, lessons, quizzes, progress,
│   │   │                  # notes, certificates, chat, admin
│   │   ├── services/      # ai_tutor, code_checker, certificate_gen
│   │   ├── seed/          # lesson content + database seed runner
│   │   └── main.py        # FastAPI app entrypoint
│   └── alembic/           # database migrations
├── frontend/
│   └── src/
│       ├── api/           # axios client + endpoint functions
│       ├── context/       # Auth + AppSettings (theme/language) contexts
│       ├── components/    # Layout, ProtectedRoute
│       └── pages/         # 11 pages (Landing, Login, Dashboard, ...)
├── lessons/                # (reserved for exported/static lesson content)
├── quizzes/                 # (reserved for exported/static quiz content)
├── certificates/            # generated certificate PDFs land here
├── docker/                  # Dockerfiles + docker-compose.yml
├── scripts/                 # run_backend / run_frontend / start_all (.sh + .bat)
├── docs/                    # deployment guides
├── prompts/                  # AI tutor prompt reference notes
├── requirements.txt
└── .env.example
```

---

## 🚀 Quick Start

### Option A — One command (Linux / macOS / Termux)

```bash
git clone <your-repo-url> kabiru-ai-tutor
cd kabiru-ai-tutor
bash scripts/start_all.sh
```

This creates a Python virtual environment, installs backend dependencies, seeds the database with
all 70 lessons and quizzes, installs frontend dependencies, and starts both servers:
- Backend: http://localhost:8000 (interactive docs at `/docs`)
- Frontend: http://localhost:5173

### Option B — One command (Windows)

```cmd
scripts\start_all.bat
```

This opens two windows — one for the backend, one for the frontend.

### Option C — Run backend and frontend separately

```bash
# Terminal 1
bash scripts/run_backend.sh

# Terminal 2
bash scripts/run_frontend.sh
```

(Windows: use `run_backend.bat` and `run_frontend.bat` instead.)

### Option D — Docker

```bash
docker compose -f docker/docker-compose.yml up --build
```

---

## 📱 Running on Android (Termux)

1. Install [Termux](https://termux.dev) from F-Droid.
2. Install prerequisites:
   ```bash
   pkg update
   pkg install python git nodejs
   ```
3. Clone the project and run:
   ```bash
   bash scripts/start_all.sh
   ```
4. Open `http://localhost:5173` in your phone's browser.

## 📱 Running on Android (Pydroid 3)

1. Install **Pydroid 3** and the **Pydroid Repository Plugin** from the Play Store.
2. Inside Pydroid's terminal (Pip tab), install: `fastapi`, `uvicorn`, `sqlalchemy`, `alembic`,
   `python-jose`, `passlib`, `bcrypt`, `python-multipart`, `python-dotenv`, `httpx`, `email-validator`,
   `reportlab`.
3. Open `backend/app/main.py` and run it, or use Pydroid's terminal to run:
   ```bash
   cd backend
   python -m app.seed.run_seed
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
4. For the frontend, either run it on a separate machine pointed at your phone's IP, or use Termux
   alongside Pydroid for the Node.js frontend server.

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` and adjust as needed:

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | JWT signing secret — **change this before production** | insecure dev key |
| `DATABASE_URL` | SQLAlchemy database URL | `sqlite:///./kabiru_tutor.db` |
| `OLLAMA_ENABLED` | Whether to try using a local Ollama model | `true` |
| `OLLAMA_BASE_URL` | URL of your local Ollama server | `http://localhost:11434` |
| `OLLAMA_MODEL` | `auto` to auto-pick the best installed model, or an exact model name to force one | `auto` |
| `OLLAMA_PREFERRED_MODELS` | Priority order used when `OLLAMA_MODEL=auto`, comma-separated | `qwen,deepseek,llama,gemma,mistral` |
| `FRONTEND_ORIGIN` | Allowed CORS origin for the frontend | `http://localhost:5173` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT expiry | `1440` (24 hours) |
| `WEBAUTHN_RP_ID` | Bare domain the frontend is served from (Face ID / Touch ID login) | `localhost` |
| `WEBAUTHN_ORIGIN` | Exact frontend URL(s), comma-separated | `http://localhost:5173` |

**Face ID / Touch ID login (WebAuthn):** in production, set `WEBAUTHN_RP_ID` to your frontend's bare
domain (e.g. `kabiru-tutor.vercel.app`, no `https://`) and `WEBAUTHN_ORIGIN` to the exact URL(s)
users load the app from. Getting these wrong is the most common cause of "Registration failed" —
see the warnings the backend logs on startup if they're still on their `localhost` defaults.

If Ollama isn't installed or isn't running, the app **automatically falls back** to a built-in
rule-based tutor — no functionality is lost, responses are just less flexible.

To enable the full local AI model:
```bash
# Install Ollama: https://ollama.com/download
ollama pull qwen2.5:7b      # or any model you prefer — auto-detected, no config needed
ollama serve
```

---

## 🗄️ Database & Migrations

The app auto-creates all tables on first run (SQLite). For schema changes going forward, use Alembic:

```bash
cd backend
alembic upgrade head          # apply migrations
alembic revision --autogenerate -m "description"   # create a new migration
```

To (re-)populate the database with all lesson content:
```bash
cd backend
python -m app.seed.run_seed
```
This is **idempotent** — safe to run any number of times without creating duplicate data.

---

## 🔌 API Overview

Interactive documentation is auto-generated at **`/docs`** once the backend is running. Key route
groups:

| Prefix | Purpose |
|---|---|
| `/api/auth` | register, login, get/update current user |
| `/api/auth/webauthn` | Face ID / Touch ID / Windows Hello passkey registration & login |
| `/api/courses` | list/get courses |
| `/api/lessons` | get/search lessons, mark complete, recommend next |
| `/api/quizzes` | get/submit quizzes, view past attempts |
| `/api/progress` | dashboard summary, streak tracking |
| `/api/notes` | CRUD for personal notes |
| `/api/certificates` | issue and download certificates |
| `/api/chat` | AI tutor chat, error explanation, code checking |
| `/api/admin` | manage users, courses, lessons, quizzes (admin only) |

---

## 🧪 Testing the Backend

```bash
cd backend
python -m pytest
```
(Add your own test files under `backend/tests/` — a `TestClient`-based example is taught in FastAPI
lesson 13 of the course itself.)

---

## 🌍 Deployment

See [`docs/DEPLOYMENT_RENDER.md`](docs/DEPLOYMENT_RENDER.md) and
[`docs/DEPLOYMENT_RAILWAY.md`](docs/DEPLOYMENT_RAILWAY.md) for step-by-step guides to deploying the
backend and frontend to free-tier cloud hosting.

---

## 📜 License

This project was built as a personal learning platform for Kabiru Sani. You're free to use, modify,
and extend it for your own learning.

---

Built with ❤️ for Kabiru Sani — Nigeria 🇳🇬
