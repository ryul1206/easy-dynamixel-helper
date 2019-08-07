# Easy Dynamixel Helper

![PyPI](https://img.shields.io/pypi/v/dynamixel-helper.svg)
[![Downloads](https://pepy.tech/badge/dynamixel-helper)](https://pepy.tech/project/dynamixel-helper)
![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)
![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)

🌏 [English](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/README.md),
[한국어](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/README.kr.md)

This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.

```bash
pip install dynamixel_helper --user
```

**Table of Contents**

1. [ Features](#-Features)
1. [ Simple Example](#-Simple-Example)
1. [ Getting Started](#-Getting-Started)
    1. [Prerequisites](#Prerequisites)
    1. [Installation](#Installation)
1. [ Tutorials](#-Tutorials)
1. [ Release Notes](#-Release-Notes)
1. [ Coverage](#-Coverage)
    1. [Model List](#Model-List)
    1. [Control Table](#Control-Table)
1. [ Contributing](#-Contributing)
    1. [Style Guide](#Style-Guide)
1. [ Maintainers](#-Maintainers)
1. [ Licenses](#-Licenses)

## 💎 Features

- Baud rate auto-matching
- Protocol auto-matching
- Port auto-matching (*Easy connections in multi-USB*)
- Motor configurations in JSON format
- Support for Python 3 and 2
- Make your code simple and clean
- **Easy to use even for beginners.**

## 🐣 Simple Example

The following code is an example of turning on the motor torque.

```python
from dynamixel_helper import DxlHelper

helper = DxlHelper("preset/{my_robot}.json")
motor = helper.get_motor(0)  # id: 0
motor.set_torque(True)
```

## 🚀 Getting Started

### Prerequisites

1. **pip (package manager)**

    ```bash
    # Python 2
    sudo apt install python-pip
    python -m pip install -U pip
    # Python 3
    sudo apt install python3-pip
    python3 -m pip install -U pip
    ```

2. **Dynamixel SDK**

    **CAUTION💥**: Please install the `pip` **before** installing the `Dynamixel SDK`. Otherwise, when you install this `Dynamixel Helper`, you will get an dependency error of `Dynamixel SDK`.

    You need to install the official [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) before using this helper.

    <details><summary>Click here: Dynamixel SDK Installation</summary>
    <p>

    1. Clone the official SDK repository into your custom folder, for example, I created `~/lib`.

        ```bash
        git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
        ```

    2. Go into the folder `/DynamixelSDK/python` of your cloned SDK.

        ```bash
        cd ${your_download_path}/DynamixelSDK/python
        ```

    3. Run `setup.py` with `--user` option to install the library. Administrator privileges, a.k.a. `sudo`, are not recommended. More information [here](https://pages.charlesreid1.com/dont-sudo-pip/).

        ```bash
        python setup.py install --user
        ```

    </p>
    </details>

### Installation

Simply type `pip` command below to install this helper.

```bash
pip install dynamixel_helper --user
```

## 🌱 Tutorials

[Go to tutorials](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/tutorial/TUTORIAL.en.md)

## 🚩 Release Notes


[Go to release notes](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/CHANGELOG.md#Release-Notes)

## 🔭 Coverage

**v1.0.0**

### Model List

- [XM430-W210](http://emanual.robotis.com/docs/en/dxl/x/xm430-w210/#control-table-of-eeprom-area)
- [XL430-W250](http://emanual.robotis.com/docs/en/dxl/x/xl430-w250/#control-table-of-eeprom-area)

### Control Table

Different models have slightly different control tables. Please check the documentation for each model. Just click the model name above to go to the document.

- EEPROM section
    - drive mode (w)
    - operating mode (w)
- RAM section
    - torque (r/w)
    - goal velocity (w)
    - goal position (w)
    - present velocity (r)
    - present position (r)

## 💌 Contributing

- We will welcome whatever your contribution is!
- If you are planning to send a new `Pull request`, please send them into the `develop` Branch.😍
### Style Guide

> This style guide is only a recommendation, never more important than your interest and contributions.

- Our default Python style is [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- If you use [VSCode](https://code.visualstudio.com/) as your code editor, please refer to the following settings. This setting is a part of our `setting.json`.

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

## 🔧 Maintainers

- **Hong-ryul Jung** _Initial work_ [ryul1206](https://github.com/ryul1206)
- **Il-ho Oh** _Initial work_ [ohilho](https://github.com/ohilho)

## 📜 Licenses

The contents of this repository are subject to the [MIT License](https://github.com/ryul1206/easy-dynamixel-helper/blob/master/LICENSE) by default, except as noted below.

- Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)

