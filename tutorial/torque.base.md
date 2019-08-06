<!---------------------------->
<!-- multilangual suffix: en, kr -->
<!---------------------------->

<!-- [en] -->
# Torque On/Off
<!-- [kr] -->
# 토크 켜기/끄기
<!-- [common] -->

🌏 [English](torque.en.md), [한국어](torque.kr.md)

<!-- [en] -->
- Next Tutorial: [Multiple USB ports](multiple_ports.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)
<!-- [kr] -->
- 다음 튜토리얼: [다중 USB 포트](multiple_ports.kr.md)
- [튜토리얼 전체 목차로 돌아가기](TUTORIAL.kr.md)
<!-- [common] -->

---

<!-- [en] -->
In the previous tutorial, we created `my_preset.json` for one motor. Now we are going to change the torque of this motor.

> Make sure the motor power is on before executing the code below.
<!-- [kr] -->
이전 튜토리얼에서 하나의 모터를 위한 `my_preset.json`을 만들었습니다. 이제 우리는 이 모터의 토크를 변경해보겠습니다.

> 아래의 코드를 실행하기 전에 모터의 전원이 켜져 있는지 확인하세요.
<!-- [common] -->

```python
from dynamixel_helper import DxlHelper

helper = DxlHelper("my_preset.json")

motor_id = 0
motor = helper.get_motor(motor_id)
motor.set_torque(True)
```

<!-- [en] -->
Since the program was terminated without turning off the torque, the torque of the motor will remain on. You can turn off the torque simply by replacing the last line above with:
<!-- [kr] -->
토크를 끄지 않고 프로그램이 종료되었기 때문에, 모터의 토크는 계속 켜져 있을 것입니다. 위의 마지막 줄을 다음과 같이 바꾸면 간단하게 토크를 끌 수 있습니다.
<!-- [common] -->

```python
motor.set_torque(False)
```

---

<!-- [en] -->
- Next Tutorial: [Multiple USB ports](multiple_ports.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)
<!-- [kr] -->
- 다음 튜토리얼: [다중 USB 포트](multiple_ports.kr.md)
- [튜토리얼 전체 목차로 돌아가기](TUTORIAL.kr.md)
<!-- [common] -->
