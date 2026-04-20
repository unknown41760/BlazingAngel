import mujoco

XML = """
<mujoco>
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


def main():
    # This is a minimal free-body example, not a controllable hopper yet.
    model = mujoco.MjModel.from_xml_string(XML)
    data = mujoco.MjData(model)

    for step in range(1000):
        mujoco.mj_step(model, data)
        print(f"Step {step}: z-position = {data.qpos[2]:.3f}")

    print("Simulation complete!")


if __name__ == "__main__":
    main()
