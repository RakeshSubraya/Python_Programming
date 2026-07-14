import shutil
from pathlib import Path

ROOT_VENV = Path(r"F:\Project\Python Programming\.venv")
TARGET_VENV = Path(__file__).resolve().parent / ".venv"

if not ROOT_VENV.exists():
    raise SystemExit(f"Root venv not found at {ROOT_VENV}")

if TARGET_VENV.exists():
    print(f"Removing existing target venv: {TARGET_VENV}")
    shutil.rmtree(TARGET_VENV)

print(f"Copying root venv from {ROOT_VENV} to {TARGET_VENV}")
shutil.copytree(ROOT_VENV, TARGET_VENV)

pyvenv_cfg = TARGET_VENV / "pyvenv.cfg"
if pyvenv_cfg.exists():
    text = pyvenv_cfg.read_text(encoding="utf-8")
    lines = []
    for line in text.splitlines():
        if line.startswith("home = "):
            lines.append("home = C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312")
        else:
            lines.append(line)
    pyvenv_cfg.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {pyvenv_cfg}")

print("Environment copy complete. Run .venv\\Scripts\\python.exe main.py from expense-agent.")