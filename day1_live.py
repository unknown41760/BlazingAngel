import argparse
import time

import mujoco
import mujoco.viewer

from day1 import configure_camera, make_model_and_data


def main():
    parser = argparse.ArgumentParser(description="Run the MuJoCo demo in a live viewer.")
    parser.add_argument(
        "--duration-seconds",
        type=float,
        default=None,
        help="Optional auto-close timer for the live viewer.",
    )
    args = parser.parse_args()

    model, data = make_model_and_data()

    with mujoco.viewer.launch_passive(model, data) as viewer:
        with viewer.lock():
            configure_camera(viewer.cam)
        viewer.sync()

        start_time = time.time()
        while viewer.is_running():
            step_start = time.time()
            mujoco.mj_step(model, data)
            viewer.sync()

            if args.duration_seconds is not None and time.time() - start_time >= args.duration_seconds:
                break

            remaining = model.opt.timestep - (time.time() - step_start)
            if remaining > 0:
                time.sleep(remaining)


if __name__ == "__main__":
    main()
