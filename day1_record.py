import argparse
from pathlib import Path

import mediapy as media
import mujoco

from day1 import configure_camera, make_model_and_data


def main():
    parser = argparse.ArgumentParser(description="Record the MuJoCo demo to a video file.")
    parser.add_argument("--output", default="outputs/day1.mp4", help="Video output path.")
    parser.add_argument("--duration-seconds", type=float, default=5.0, help="Video duration.")
    parser.add_argument("--fps", type=int, default=60, help="Frames per second.")
    parser.add_argument("--width", type=int, default=960, help="Video width.")
    parser.add_argument("--height", type=int, default=540, help="Video height.")
    args = parser.parse_args()

    model, data = make_model_and_data()
    camera = mujoco.MjvCamera()
    configure_camera(camera)
    renderer = mujoco.Renderer(model, height=args.height, width=args.width)

    total_frames = max(1, int(args.duration_seconds * args.fps))
    steps_per_frame = max(1, round((1 / args.fps) / model.opt.timestep))
    frames = []

    for _ in range(total_frames):
        mujoco.mj_step(model, data, nstep=steps_per_frame)
        renderer.update_scene(data, camera=camera)
        frames.append(renderer.render().copy())

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    media.write_video(output_path, frames, fps=args.fps)
    print(f"Saved video to {output_path.resolve()}")


if __name__ == "__main__":
    main()
