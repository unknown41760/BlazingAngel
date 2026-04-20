import mujoco

XML = """
<mujoco>
  <visual>
    <global offwidth="1920" offheight="1080"/>
  </visual>
  <worldbody>
    <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="1 1 0.1" rgba=".9 0.9 0.9 1"/>
    <body name="torso" pos="0 0 1">
      <joint type="free"/>
      <geom type="capsule" fromto="0 0 0 0 0 0.5" size="0.05"/>
    </body>
  </worldbody>
</mujoco>
"""


def make_model_and_data():
    model = mujoco.MjModel.from_xml_string(XML)
    data = mujoco.MjData(model)
    return model, data


def configure_camera(camera):
    camera.type = mujoco.mjtCamera.mjCAMERA_FREE
    camera.lookat[:] = [0.0, 0.0, 0.3]
    camera.distance = 2.5
    camera.azimuth = 135
    camera.elevation = -20


def main():
    # This is a minimal free-body example, not a controllable hopper yet.
    model, data = make_model_and_data()

    for step in range(1000):
        mujoco.mj_step(model, data)
        print(f"Step {step}: z-position = {data.qpos[2]:.3f}")

    print("Simulation complete!")


if __name__ == "__main__":
    main()
