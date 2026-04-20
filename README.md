# BlazingAngel

Minimal MuJoCo simulation example.

## Setup

```powershell
uv venv venv-ai
uv pip install --python "venv-ai\Scripts\python.exe" -r requirements.txt
```

## Run

```powershell
& "venv-ai\Scripts\python.exe" "day1.py"
```

`mujoco==3.2.5` is pinned because `mujoco==3.7.0` fails on this Windows machine with `WinError 1114` during `import mujoco`.
