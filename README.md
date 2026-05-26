<div align="left">
  <img src="pace.jpg" alt="Pace 1.0" width="55%">
</div>
<br>

# Pace-Architex
Semi Capable open source local AI model under 800mb<br>
Added coding capability and self loop checking <br>
Lite version of pace designed to have a GUI<br>
Added internet search, allowing for more relevant answers. <br><br>
Debugging Script: <br>
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python pace.py
```

# QuickStart
Basically just download entire thing and unzip to your USB or local drive. <br><br>Run:
- `pace-windows.bat` on Windows
- `pace-mac.command` on macOS
- `pace-linux.sh` on Linux

All launchers now call `pace-portable.py`, which keeps setup inside this folder (`.venv` + `.pace_agent`), opens the GUI, and starts the backend from a single click. <br>
Additionally, if huggingface is blocked, you can download Gemma from the releases section of this repo and drop it straight into `.pace_agent`

## Main Pace Repo
Main: https://github.com/Katsugachi/Pace-1.0/tree/main<br>
Lite: https://github.com/Katsugachi/Pace-Lite-1.0<br>
Architex: https://github.com/Katsugachi/Pace-1.0-Architex/tree/main

## Start
Basically just download entire thing and unzip to USB or local storage. <br><br>Run `pace-windows.bat` for Windows, `pace-mac.command` for macOS, or `pace-linux.sh` for Linux. The one-click launcher flow is fully relative-path based, so moving the folder between drives keeps it runnable.

### Portable USB note
- For offline dependency install, optionally add a `wheelhouse/` folder next to `pace-portable.py` containing required wheels (currently `websockets` and its transitive wheels for your target OS/Python).
- `llama-cpp-python` is still platform/compiler-specific and remains a manual install when needed, as documented in messages printed by `dev-pace.py` at startup.
## Model setup note
The GUI can now connect even if the local model is unavailable, but full responses still require `llama-cpp-python` to be installed successfully. If the backend starts in degraded mode, follow the setup instructions printed in the terminal, then restart `dev-pace.py`.

## Internet mode toggle
PACE can now run in two internet modes:
- **Web On**: uses live internet research (tutorials, coding docs, CDNs, and other web sources).
- **Web Off**: uses only local model knowledge, better from creative writing and tasks not requiring web sources

You can toggle this in both places:
- **GUI**: use the `Web On` / `Web Off` button in the header.
- **Terminal**: use `/internet on`, `/internet off`, `/internet toggle`, or `/internet status`.

When Web mode is on, Pace now only uses internet research when the prompt appears to need external/current references (for example docs, tutorials, API/version/current-event lookups). Simple greetings and creative/narrative writing stay local.
