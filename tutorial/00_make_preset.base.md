<!---------------------------->
<!-- multilangual suffix: en, kr -->
<!---------------------------->

<!-- [en] -->
# Define Motors in `preset.json`
<!-- [kr] -->
# `preset.json`으로 모터 정의하기
<!-- [common] -->

<!-- [en] -->
- Next Tutorial: [Torque On/Off](01_torque.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)
<!-- [kr] -->
- 다음 튜토리얼: [토크 켜기/끄기](01_torque.kr.md)
- [튜토리얼 전체 목차로 돌아가기](TUTORIAL.kr.md)
<!-- [common] -->

---

<!-- [kr] -->
## 프리셋 파일의 용도

프리셋 파일은 모터와 포트에 대한 정보를 적어두는 곳입니다. 그러면 헬퍼가 알아서 프리셋 파일을 분석하고 모터를 사용할 수 있도록 준비를 마칩니다.

## 프리셋이 필요한 이유

모터를 컴퓨터와 연결하려면 포트(port) 이름, 보드레이트(baud rate), 프로토콜(protocol), 모터의 모델명, 어떤 모터가 어느 포트에 꼽혀 있는지 등등... 많은 머리 귀찮은 것들을 알아야 합니다. 그리고 물론 프로그램 코드에도 이러한 것들을 적어야 합니다.

하지만 이러한 환경설정들을 코드에 적으면 코드가 매우 지저분해지는 문제가 있습니다. 그리고 환경설정은 로봇을 바꾸지 않으면 수정할 일이 거의 없습니다. 그래서 각종 설정들을 별도의 파일로 따로 빼두는 것이 깨끗할 뿐만 아니라 안전합니다. 코드를 수정하다가 실수로 바꿀 일도 없으니까요.

## 프리셋의 형태

프리셋 파일의 기본 형태를 아래와 같습니다.
<!-- [common] -->

```json
{
  "ports":[  ],
  "baud rates":[  ],
  "protocol versions":[  ],
  "motors":[  ]
}
```

<!-- [kr] -->
위와 같은 형태의 파일을 [json 파일](https://ko.wikipedia.org/wiki/JSON)이라고 합니다. json을 처음 접하더라도 걱정하지 마세요. json은 사람이 쉽게 데이터를 이해할 수 있도록 만들어진 것이니까요.

### 구성 요소

<!-- [common] -->
1. "ports"
1. "baud rates"
1. "protocol versions"
1. "motors"

<!-- [kr] -->
### 완성된 프리셋

<!-- [common] -->
```json
{
  "ports":[ "/dev/ttyUSB0" ],
  "baud rates":[ 57600 ],
  "protocol versions":[ 2.0 ],
  "motors":[
    {
      "id": 0,
      "alias": "joint_1",
      "model": "XM430-W210"
    }
  ]
}
```

---

<!-- [en] -->
- Next Tutorial: [Torque On/Off](01_torque.en.md)
- [Back to the tutorial front page](TUTORIAL.en.md)
<!-- [kr] -->
- 다음 튜토리얼: [토크 켜기/끄기](01_torque.kr.md)
- [튜토리얼 전체 목차로 돌아가기](TUTORIAL.kr.md)
<!-- [common] -->
