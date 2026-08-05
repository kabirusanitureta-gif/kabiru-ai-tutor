@echo off
REM Kabiru AI Tutor — Start Everything (Windows)
setlocal

set SCRIPT_DIR=%~dp0

echo === Kabiru AI Tutor: Starting full stack ===
echo Backend:  http://localhost:8000  (docs at /docs)
echo Frontend: http://localhost:5173
echo.
echo Each server opens in its own window. Close those windows to stop them.
echo.

start "Kabiru AI Tutor - Backend" cmd /k "%SCRIPT_DIR%run_backend.bat"

timeout /t 4 /nobreak >nul

start "Kabiru AI Tutor - Frontend" cmd /k "%SCRIPT_DIR%run_frontend.bat"

endlocal
