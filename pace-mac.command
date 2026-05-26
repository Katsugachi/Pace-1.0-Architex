#!/bin/bash
set -e

# Go to the directory this script lives in (like %~dp0)
cd "$(cd "$(dirname "$0")" && pwd)"

if command -v python3.12 >/dev/null 2>&1; then
  PYTHON_BIN="python3.12"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Could not find Python 3. Install Python 3 and try again."
  read -r -p "Press Enter to exit..."
  exit 1
fi

"$PYTHON_BIN" "pace-portable.py"
EXIT_CODE=$?
read -r -p "Press Enter to exit..."
exit "$EXIT_CODE"
