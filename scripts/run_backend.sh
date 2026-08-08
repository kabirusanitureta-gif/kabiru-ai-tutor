#!/usr/bin/env bash
# Kabiru AI Tutor — Backend Runner
# Works on Linux, macOS, and Android Termux.
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"

echo "=== Kabiru AI Tutor: Backend Setup ==="

cd "$BACKEND_DIR"

# 1. Create a virtual environment if it doesn't exist yet.
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv || python -m venv venv
fi

# 2. Activate it.
# shellcheck disable=SC1091
source venv/bin/activate

# 3. Install/update dependencies.
echo "Installing dependencies..."
pip install --upgrade pip --quiet
pip install -r "$ROOT_DIR/requirements.txt" --quiet

# 4. Copy .env.example to .env on first run if missing.
if [ ! -f "$ROOT_DIR/.env" ]; then
    echo "Creating .env from .env.example..."
    cp "$ROOT_DIR/.env.example" "$ROOT_DIR/.env"
fi

# 5. Seed the database with courses/lessons/quizzes (idempotent — safe to re-run).
echo "Seeding database (idempotent)..."
python -m app.seed.run_seed

# 6. Start the FastAPI server.
echo "Starting backend on http://0.0.0.0:8000 (docs at /docs)..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
