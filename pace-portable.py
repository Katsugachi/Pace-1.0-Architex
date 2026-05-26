#!/usr/bin/env python3
import os
import subprocess
import sys
import venv
import webbrowser
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
VENV_DIR = ROOT_DIR / ".venv"
VENV_PYTHON = VENV_DIR / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
WHEELHOUSE_DIR = ROOT_DIR / "wheelhouse"
BACKEND_SCRIPT = ROOT_DIR / "dev-pace.py"
GUI_FILE = ROOT_DIR / "index.html"
BROWSER_OPEN_NEW_TAB = 2


def ensure_virtualenv() -> None:
    if VENV_PYTHON.exists():
        return
    print("Setting up environment for the first time...")
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(VENV_DIR)


def has_module(module_name: str) -> bool:
    result = subprocess.run(
        [str(VENV_PYTHON), "-c", f"import {module_name}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def install_dependencies() -> None:
    if has_module("websockets"):
        return

    pip_base_cmd = [str(VENV_PYTHON), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"]
    subprocess.check_call(pip_base_cmd)

    if WHEELHOUSE_DIR.is_dir():
        print("Using local wheelhouse for portable USB install...")
        subprocess.check_call(
            [
                str(VENV_PYTHON),
                "-m",
                "pip",
                "install",
                "--no-index",
                f"--find-links={WHEELHOUSE_DIR}",
                "websockets",
            ]
        )
    else:
        subprocess.check_call([str(VENV_PYTHON), "-m", "pip", "install", "websockets"])


def open_gui() -> None:
    webbrowser.open(GUI_FILE.resolve().as_uri(), new=BROWSER_OPEN_NEW_TAB)


def run_backend() -> int:
    process = subprocess.run([str(VENV_PYTHON), str(BACKEND_SCRIPT)], cwd=str(ROOT_DIR))
    return process.returncode


def main() -> int:
    os.chdir(ROOT_DIR)
    if not BACKEND_SCRIPT.exists() or not GUI_FILE.exists():
        print("Missing required project files. Run this from the Pace project folder.")
        return 1
    ensure_virtualenv()
    install_dependencies()
    open_gui()
    return run_backend()


if __name__ == "__main__":
    raise SystemExit(main())
