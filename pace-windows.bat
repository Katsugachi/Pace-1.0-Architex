@echo off
cd /d "%~dp0"
setlocal

set "PY_CMD="
py -3.12 --version >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3.12"
if not defined PY_CMD (
    py -3 --version >nul 2>nul
    if %errorlevel%==0 set "PY_CMD=py -3"
)
if not defined PY_CMD (
    python --version >nul 2>nul
    if %errorlevel%==0 set "PY_CMD=python"
)

if not defined PY_CMD (
    echo Could not find Python 3. Install Python 3 and try again.
    set "EXIT_CODE=1"
    goto :finish
)

%PY_CMD% "%~dp0pace-portable.py"
set "EXIT_CODE=%errorlevel%"

:finish
pause
exit /b %EXIT_CODE%
