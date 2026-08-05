#!/usr/bin/env bash
# Kabiru AI Tutor — Start Everything
# Runs backend and frontend together. Press Ctrl+C to stop both.
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Kabiru AI Tutor: Starting full stack ==="
echo "Backend:  http://localhost:8000  (docs at /docs)"
echo "Frontend: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both servers."
echo ""

# Start backend in the background, capturing its PID.
bash "$SCRIPT_DIR/run_backend.sh" &
BACKEND_PID=$!

# Give the backend a moment to seed the DB and boot before the frontend starts.
sleep 4

# Start frontend in the background, capturing its PID.
bash "$SCRIPT_DIR/run_frontend.sh" &
FRONTEND_PID=$!

# Ensure both child processes are terminated when this script exits.
cleanup() {
    echo ""
    echo "Stopping servers..."
    kill "$BACKEND_PID" 2>/dev/null || true
    kill "$FRONTEND_PID" 2>/dev/null || true
    wait "$BACKEND_PID" 2>/dev/null || true
    wait "$FRONTEND_PID" 2>/dev/null || true
    echo "Stopped."
}
trap cleanup EXIT INT TERM

wait "$BACKEND_PID" "$FRONTEND_PID"
