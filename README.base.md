<!---------------------------->
<!-- multilangual suffix: en, kr -->
<!-- no suffix: en -->
<!---------------------------->

<!-- [en] -->
# Easy Dynamixel Helper
<!-- [kr] -->
# 쉬운 다이나믹셀 헬퍼
<!-- [common] -->

[![PyPI](https://img.shields.io/pypi/v/dynamixel-helper.svg)](https://pypi.org/project/dynamixel-helper/)
[![Downloads](https://pepy.tech/badge/dynamixel-helper)](https://pepy.tech/project/dynamixel-helper)
[![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)

🌏 [English](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/README.md),
[한국어](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/README.kr.md)

<!-- [en] -->
This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works. In other words, this helper makes it easy to modify the control table.
<!-- [kr] -->
이 헬퍼는 다이나믹셀 SDK를 래핑(wrapping)한 것입니다. 다이나믹셀 SDK를 어떻게 사용하는지 몰라도 쉽게 모터를 설정하고 구동할 수 있도록 만들었습니다. 다시 말해, 이 헬퍼는 컨트롤 테이블을 쉽게 수정할 수 있도록 도와줍니다.
<!-- [common] -->

```bash
pip install dynamixel_helper --user
```

<!-- [ignore] -->
<!-- TODO: update figure (direct writing on the control table) -->
<!-- Your code ===> DXL Helper ===> Your motor(control table) -->

<!-- [en] -->
**Table of Contents**
<!-- [kr] -->
**목차**
<!-- [common] -->

<!-- [[ multilangual toc: no-emoji level=2~3 ]] -->

<!-- [ignore] -->
<!-- README-Template.md -->
<!-- https://gist.github.com/PurpleBooth -->

<!-- [en] -->
## 💎 Features
<!-- [kr] -->
## 💎 특징들
<!-- [common] -->

<!-- [en] -->
- Baud rate auto-matching
- Protocol auto-matching
- Port auto-matching (*Easy connections in multi-USB*)
<!-- [kr] -->
- 보드레이트 자동 매칭
- 프로토콜 자동 매칭
- 포트 자동 매칭 (*쉬워진 다중 USB 연결*)
<!-- [en] -->
- Motor configurations in JSON format
- Support for Python 3 and 2
<!-- [kr] -->
- 파이썬 3 및 2 지원
- JSON 형태로 모터 환경설정
<!-- [en] -->
- Make your code simple and clean
- **Easy to use even for beginners.**
<!-- [kr] -->
- 여러분의 코드를 간결하게 만들어 줍니다.
- **초보자도 사용하기가 쉽습니다.**
<!-- [common] -->

<!-- [en] -->
## 🐣 Simple Example
<!-- [kr] -->
## 🐣 간단한 예제
<!-- [common] -->

<!-- [en] -->
The following code is an example of turning on the motor torque.
<!-- [kr] -->
아래의 코드는 모터의 토크를 켜는 예제입니다.
<!-- [common] -->

```python
from dynamixel_helper import DxlHelper

helper = DxlHelper("preset/{my_robot}.json")
motor = helper.get_motor(0)  # id: 0
motor.set_torque(True)
```

<!-- [en] -->
## 🚀 Getting Started
<!-- [kr] -->
## 🚀 시작하기
<!-- [common] -->

<!-- [en] -->
### Prerequisites
<!-- [kr] -->
### 사전에 필요한 것
<!-- [common] -->

<!-- [en] -->
1. **pip (package manager)**
<!-- [kr] -->
1. **pip (파이썬 패키지 관리자)**
<!-- [common] -->

<!-- [en] -->
    ```bash
    # Python 2
    sudo apt install python-pip
    python -m pip install -U pip
    # Python 3
    sudo apt install python3-pip
    python3 -m pip install -U pip
    ```
<!-- [kr] -->
    ```bash
    # 파이썬 2
    sudo apt install python-pip
    python -m pip install -U pip
    # 파이썬 3
    sudo apt install python3-pip
    python3 -m pip install -U pip
    ```
<!-- [common] -->

2. **Dynamixel SDK**

<!-- [en] -->
    **CAUTION💥**: Please install the `pip` **before** installing the `Dynamixel SDK`. Otherwise, when you install this `Dynamixel Helper`, you will get an dependency error of `Dynamixel SDK`.

    You need to install the official [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) before using this helper.

    <details><summary>Click here: Dynamixel SDK Installation</summary>
    <p>

    1. Clone the official SDK repository into your custom folder, for example, I created `~/lib`.
<!-- [kr] -->
    **주의💥**: 반드시 `Dynamixel SDK`를 설치하기 **전에** `pip`부터 설치하여 주세요. 그렇지 않으면 `Dynamixel Helper`를 설치할 때 `Dynamixel SDK`를 찾을 수 없다는 의존성 오류가 발생합니다.
    
    헬퍼를 설치하기 전에 로보티즈 사에서 제공하는 공식 [다이나믹셀 SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK)가 있어야 합니다.

    <details><summary>클릭하여 보기: 다이나믹셀 SDK 설치 방법</summary>
    <p>
    
    1. 라이브러리를 설치할 공간에 공식 SDK 코드를 내려받습니다. 예를 들어, 저는 `~/lib` 폴더를 만들었습니다.
<!-- [common] -->

        ```bash
        git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
        ```

<!-- [en] -->
    2. Go into the folder `/DynamixelSDK/python` of your cloned SDK.

        ```bash
        cd ${your_download_path}/DynamixelSDK/python
        ```

    3. Run `setup.py` with `--user` option to install the library. Administrator privileges, a.k.a. `sudo`, are not recommended. More information [here](https://pages.charlesreid1.com/dont-sudo-pip/).
<!-- [kr] -->
    2. 방금 내려받은 SDK 폴더에서 `/DynamixelSDK/python` 위치로 이동합니다.

        ```bash
        cd ${여러분의_다운로드_경로}/DynamixelSDK/python
        ```
        
    3. `--user` 옵션과 함께 `setup.py`를 실행하면 SDK 설치가 끝납니다. 흔히 `sudo`라고 하는 관리자 권한은 추천하지 않습니다. 자세한 이유은 [이 글(한국어)](https://medium.com/@chullino/sudo-%EC%A0%88%EB%8C%80-%EC%93%B0%EC%A7%80-%EB%A7%88%EC%84%B8%EC%9A%94-8544aa3fb0e7)을 참고해 주세요.
<!-- [common] -->

        ```bash
        python setup.py install --user
        ```

    </p>
    </details>

<!-- [en] -->
### Installation
<!-- [kr] -->
### 설치
<!-- [common] -->

<!-- [en] -->
Simply type `pip` command below to install this helper.
<!-- [kr] -->
헬퍼의 설치는 간단히 `pip` 명령만 하면 됩니다.
<!-- [common] -->

```bash
pip install dynamixel_helper --user
```

<!-- [en] -->
## 🌱 Tutorials
<!-- [kr] -->
## 🌱 튜토리얼
<!-- [common] -->

<!-- [en] -->
[Go to tutorials](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/tutorial/TUTORIAL.en.md)
<!-- [kr] -->
[튜토리얼로 이동](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/tutorial/TUTORIAL.kr.md)
<!-- [common] -->

<!-- [en] -->
## 🚩 Release Notes
<!-- [kr] -->
## 🚩 릴리즈 노트
<!-- [common] -->

<!-- [kr] -->
> 릴리즈 노트는 기복적으로 영어로만 제공될 계획입니다. 그래도 몇가지 중요한 항목은 한글로도 제공하려 합니다.
<!-- [common] -->

[Go to release notes](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/CHANGELOG.md#Release-Notes)

<!-- [en] -->
## 🔭 Current Coverage
<!-- [kr] -->
## 🔭 현재의 커버리지
<!-- [common] -->

<!-- [en] -->
### Model List
<!-- [kr] -->
### 모델 리스트

아래 링크된 주소는 영문판 메뉴얼이지만 로보티즈에서는 한글 메뉴얼도 제공하고 있습니다. 한글 메뉴얼은 [여기](http://emanual.robotis.com/docs/kr/)에서 확인해주세요.
<!-- [common] -->

- Tested models
  - [XM430-W210](http://emanual.robotis.com/docs/en/dxl/x/xm430-w210/#control-table-of-eeprom-area)
  - [XL430-W250](http://emanual.robotis.com/docs/en/dxl/x/xl430-w250/#control-table-of-eeprom-area)
- Non-tested models (Only the control tables are included.)
  - [AX-12W](https://emanual.robotis.com/docs/en/dxl/ax/ax-12w/#control-table-of-eeprom-area)
  - [XL-320](https://emanual.robotis.com/docs/en/dxl/x/xl320/#control-table-of-eeprom-area)

<!-- [en] -->
### Control Table

Different models have slightly different control tables. Please check the documentation for each model. Just click the model name above to go to the document.
<!-- [kr] -->
### 컨트롤 테이블

모터마다 접근할 수 있는 컨트롤 테이블이 다릅니다. 이것은 각 모터의 문서를 확인해주세요. 바로 위에서 모델 이름을 클릭하면 문서로 이동할 수 있습니다.
<!-- [common] -->

- EEPROM section
    - drive mode (w)
    - operating mode (w)
- RAM section
    - torque (r/w)
    - goal velocity (w)
    - goal position (w)
    - present velocity (r)
    - present position (r)

<!-- [en] -->
## 💌 Contributing
<!-- [kr] -->
## 💌 기여하기
<!-- [common] -->

<!-- [en] -->
- We will welcome whatever your contribution is!
- If you are planning to send a new `Pull request`, please send them into the `develop` Branch.😍
<!-- [kr] -->
- 여러분의 기여가 어떠한 내용이든 어떠한 방법이든 상관없이 언제나 환영합니다!
- 만약 `Pull request`를 보내실 계획이라면 `develop` 브랜치로 부탁드립니다.😍
<!-- common -->

<!-- [ignore] -->
//<!-- [en] -->
//### Pull Request Process
//<!-- [kr] -->
//### Pull Request 절차
//<!-- [common] -->

<!-- [en] -->
### Style Guide
<!-- [kr] -->
### 스타일 가이드
<!-- [common] -->

<!-- [en] -->
> This style guide is only a recommendation, never more important than your interest and contributions.

- Our default Python style is [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- If you use [VSCode](https://code.visualstudio.com/) as your code editor, please refer to the following settings. This setting is a part of our `setting.json`.
<!-- [kr] -->
> 이 스타일 가이드는 추천사항일 뿐입니다. 어떠한 경우에도 여러분의 관심과 기여보다 중요한 것은 아닙니다.

- 파이썬 스타일은 [PEP 8](https://www.python.org/dev/peps/pep-0008/)을 기본으로 사용합니다.
- [VSCode](https://code.visualstudio.com/)를 코드에디터로 사용한다면 아래의 세팅을 참고해주세요. 이 세팅은 저희의 `setting.json` 일부입니다.
<!-- [common] -->

    ```json
    {
        "editor.tabSize": 4,
        "[json]": {
            "editor.tabSize": 2
        },
        "python.linting.pylintEnabled": false,
        "python.linting.pep8Enabled": true,
        "python.linting.enabled": true
    }
    ```

<!-- [ignore] -->
//<!-- [en] -->
//### Code of Conduct
//<!-- [kr] -->
//### 행동 강령
//<!-- [common] -->

<!-- [en] -->
## 🔧 Maintainers
<!-- [kr] -->
## 🔧 유지 관리자
<!-- [common] -->

<!-- [en] -->
- **Hong-ryul Jung** _Initial work_ [ryul1206](https://github.com/ryul1206)
- **Il-ho Oh** _Initial work_ [ohilho](https://github.com/ohilho)
<!-- [kr] -->
- **정홍렬** _Initial work_ [ryul1206](https://github.com/ryul1206)
- **오일호** _Initial work_ [ohilho](https://github.com/ohilho)
<!-- [common] -->

<!-- [en] -->
## 📜 Licenses
<!-- [kr] -->
## 📜 라이센스
<!-- [common] -->

<!-- [en] -->
The contents of this repository are subject to the [MIT License](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/LICENSE) by default, except as noted below.
<!-- [kr] -->
이 저장소에 있는 내용은 기본적으로 [MIT License](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/LICENSE)를 따릅니다. 예외적인 항목에 대해서는 아래 목록을 보아주십시오.
<!-- [common] -->

<!-- [en] -->
- Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)
<!-- [kr] -->
- 다이나믹셀 SDK는 [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)을 따릅니다.
<!-- [common] -->

<!-- [ignore] -->
**PyPI Uploading...**

python3 setup.py sdist bdist_wheel --universal 

test upload
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

deploy
python3 -m twine upload dist/*
