# BlazingAngel

Minimal MuJoCo simulation example.

## Setup

```powershell
uv venv venv-ai
uv pip install --python "venv-ai\Scripts\python.exe" -r requirements.txt
```

## Run

Print the falling body's height:

```powershell
& "venv-ai\Scripts\python.exe" "day1.py"
```

Open a live interactive viewer window:

```powershell
& "venv-ai\Scripts\python.exe" "day1_live.py"
```

Record a video:

```powershell
& "venv-ai\Scripts\python.exe" "day1_record.py"
```

The recorder writes `outputs/day1.mp4` by default.

To auto-close the live viewer after a few seconds:

```powershell
& "venv-ai\Scripts\python.exe" "day1_live.py" --duration-seconds 5
```

To change the recorded video settings:

```powershell
& "venv-ai\Scripts\python.exe" "day1_record.py" --output "outputs/custom.mp4" --duration-seconds 3 --fps 30
```

`mujoco==3.2.5` is pinned because `mujoco==3.7.0` fails on this Windows machine with `WinError 1114` during `import mujoco`.

Recording also expects `ffmpeg` to be available on your `PATH`.
