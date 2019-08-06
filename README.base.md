<!---------------------------->
<!-- multilangual suffix: en, kr -->
<!-- no suffix: en -->
<!---------------------------->

<!-- [en] -->
# Easy Dynamixel Helper
<!-- [kr] -->
# 쉬운 다이나믹셀 헬퍼
<!-- [common] -->

![PyPI](https://img.shields.io/pypi/v/dynamixel-helper.svg)
[![Downloads](https://pepy.tech/badge/dynamixel-helper)](https://pepy.tech/project/dynamixel-helper)
![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)
![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)

🌏 [English](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/README.md),
[한국어](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/README.kr.md)

<!-- [en] -->
This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.
<!-- [kr] -->
이 헬퍼는 다이나믹셀 SDK를 래핑(wrapping)한 것입니다. 다이나믹셀 SDK를 어떻게 사용하는지 몰라도 쉽게 모터를 설정하고 구동할 수 있도록 만들었습니다.
<!-- [common] -->

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
## 🚀 Getting Started
<!-- [kr] -->
## 🚀 시작하기
<!-- [common] -->

<!-- [en] -->
### Prerequisites
<!-- [kr] -->
### 사전에 필요한 것
<!-- [common] -->

**1. pip**

- Python 2

    ```bash
    sudo apt install python-pip
    python -m pip install -U pip
    ```

- Python 3

    ```bash
    sudo apt install python3-pip
    python3 -m pip install -U pip
    ```

**2. Dynamixel SDK**

<!-- [en] -->
You need to install the official [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) before using this helper.
<!-- [kr] -->
헬퍼를 설치하기 전에 로보티즈 사에서 제공하는 공식 [다이나믹셀 SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK)가 있어야 합니다.
<!-- [common] -->

<!-- [en] -->
<details><summary>Click here: Dynamixel SDK Installation</summary>
<p>
<!-- [kr] -->
<details><summary>클릭하여 보기: 다이나믹셀 SDK 설치 방법</summary>
<p>
<!-- [common] -->

<!-- [en] -->
1. Clone the official SDK repository into your custom folder, for example, I created `~/lib`.
<!-- [kr] -->
1. 라이브러리를 설치할 공간에 공식 SDK 코드를 내려받습니다. 예를 들어, 저는 `~/lib` 폴더를 만들었습니다.
<!-- [common] -->

    ```bash
    git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    ```
<!-- [en] -->
2. Go into the folder `/DynamixelSDK/python` of your cloned SDK.
<!-- [kr] -->
2. 방금 내려받은 SDK 폴더에서 `/DynamixelSDK/python` 위치로 이동합니다.
<!-- [common] -->

    ```bash
    cd ${your_download_path}/DynamixelSDK/python
    ```

<!-- [en] -->
3. Run `setup.py` as administrator to install the library.
<!-- [kr] -->
3. 관리자 권한으로 `setup.py`를 실행하면 SDK 설치가 끝납니다.
<!-- [common] -->

    ```bash
    python setup.py install
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

helper = DxlHelper("preset/{your_robot}.json")
motor = helper.get_motor(0)  # id: 0
motor.set_torque(True)
```

<!-- [en] -->
## 💎 Features
<!-- [kr] -->
## 💎 특징들
<!-- [common] -->

<!-- [en] -->
- Motor configurations in JSON format
<!-- [kr] -->
- JSON 양식으로 모터 구성을 설정
<!-- [en] -->
- Support for Python 3 and 2
<!-- [kr] -->
- 파이썬 3 및 2 지원
<!-- [en] -->
- Easy multiple USB connections
<!-- [kr] -->
- 쉬워진 USB 다중 연결
<!-- [common] -->

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
