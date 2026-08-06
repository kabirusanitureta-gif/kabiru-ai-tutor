@echo off
REM Kabiru AI Tutor — Frontend Runner (Windows)
setlocal

set SCRIPT_DIR=%~dp0
set ROOT_DIR=%SCRIPT_DIR%..
set FRONTEND_DIR=%ROOT_DIR%\frontend

echo === Kabiru AI Tutor: Frontend Setup ===

cd /d "%FRONTEND_DIR%"

where node >nul 2>nul
if errorlevel 1 (
    echo Node.js is not installed. Download it from https://nodejs.org
    exit /b 1
)

if not exist node_modules (
    echo Installing frontend dependencies, this may take a few minutes...
    call npm install
)

echo Starting frontend dev server on http://0.0.0.0:5173 ...
call npm run dev -- --host

endlocal
