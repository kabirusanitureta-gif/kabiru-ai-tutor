#!/usr/bin/env bash
# Kabiru AI Tutor — Frontend Runner
# Works on Linux, macOS, and Android Termux (with Node.js installed via pkg install nodejs).
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
FRONTEND_DIR="$ROOT_DIR/frontend"

echo "=== Kabiru AI Tutor: Frontend Setup ==="

cd "$FRONTEND_DIR"

if ! command -v node >/dev/null 2>&1; then
    echo "Node.js is not installed."
    echo "  - Linux/macOS: install from https://nodejs.org or your package manager"
    echo "  - Termux:      run 'pkg install nodejs'"
    exit 1
fi

# Install dependencies only if node_modules is missing or package.json changed.
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies (this may take a few minutes)..."
    npm install
fi

echo "Starting frontend dev server on http://0.0.0.0:5173 ..."
npm run dev -- --host
