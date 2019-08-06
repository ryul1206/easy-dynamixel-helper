# Torque On/Off

🌏 [English](torque.en.md), [한국어](torque.kr.md)

- Next Tutorial: [Multiple USB ports](multiple_ports.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)

---

In the previous tutorial, we created `my_preset.json` for one motor. Now we are going to change the torque of this motor.

> Make sure the motor power is on before executing the code below.

```python
from dynamixel_helper import DxlHelper

helper = DxlHelper("my_preset.json")

motor_id = 0
motor = helper.get_motor(motor_id)
motor.set_torque(True)
```

Since the program was terminated without turning off the torque, the torque of the motor will remain on. You can turn off the torque simply by replacing the last line above with:

```python
motor.set_torque(False)
```

---

- Next Tutorial: [Multiple USB ports](multiple_ports.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)
