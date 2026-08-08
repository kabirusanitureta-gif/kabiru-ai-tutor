@echo off
REM Kabiru AI Tutor — Backend Runner (Windows)
setlocal

set SCRIPT_DIR=%~dp0
set ROOT_DIR=%SCRIPT_DIR%..
set BACKEND_DIR=%ROOT_DIR%\backend

echo === Kabiru AI Tutor: Backend Setup ===

cd /d "%BACKEND_DIR%"

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip --quiet
pip install -r "%ROOT_DIR%\requirements.txt" --quiet

if not exist "%ROOT_DIR%\.env" (
    echo Creating .env from .env.example...
    copy "%ROOT_DIR%\.env.example" "%ROOT_DIR%\.env"
)

echo Seeding database (idempotent)...
python -m app.seed.run_seed

echo Starting backend on http://0.0.0.0:8000 (docs at /docs)...
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

endlocal
