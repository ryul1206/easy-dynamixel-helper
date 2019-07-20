# Easy Dynamixel Helper

![PyPI](https://img.shields.io/pypi/v/dynamixel-helper.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/easy-dynamixel-helper.svg)
![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)
![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)


[English](README.md), [한국어](README(kor).md)

This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.

<!-- TODO: update figure (direct writing on the control table) -->
<!-- Your code ===> DXL Helper ===> Your motor(control table) -->

1. [Getting Started](#Getting-Started)
    1. [Prerequisites](#Prerequisites)
    2. [Installation](#Installation)
2. [Simple Example](#Simple-Example)
3. [Features](#Features)
4. [Tutorials](#Tutorials)
5. [Release Notes](#Release-Notes)
6. [Contributing](#Contributing)
7. [Maintainers](#Maintainers)
8. [Licenses](#Licenses)

<!-- README-Template.md -->
<!-- https://gist.github.com/PurpleBooth -->

## Getting Started

### Prerequisites

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

3. Run `setup.py` as administrator to install the library.

    ```bash
    sudo python setup.py install
    ```

</p>
</details>

### Installation

```bash
pip install dynamixel_helper --user
```

## Simple Example

The code below turns the motor's torque on.

```python
from dynamixel_helper import DxlHelper

helper = DxlHelper("preset/{your_robot}.json")
motor = helper.get_motor(0)  # id: 0
motor.set_torque(True)
```

## Features

- Motor configurations in JSON format
- Support for Python 2.x and 3.x
- Easy multiple USB connections

## Tutorials

[Go to tutorials](/tutorial/TUTORIAL.md)

## Release Notes

[Click here](/CHANGELOG)

## Contributing

code of ..?

<!-- vscode `setting.json`

```json
"editor.tabSize": 4,
"[json]": {
    "editor.tabSize": 2
},
"markdownlint.config": {
    "default": true,
    // "MD003": { "style": "atx_closed" },
    "MD007": { "indent": 4 },
    "no-hard-tabs": false
},
"python.linting.pylintEnabled": false,
"python.linting.pep8Enabled": true,
"python.linting.enabled": true
``` -->

## Maintainers

- **Hong-ryul Jung** _Initial work_ [ryul1206](https://github.com/ryul1206)
- **Il-ho Oh** _Initial work_ [ohilho](https://github.com/ohilho)

## Licenses

The contents of this repository are subject to the [MIT license](/LICENSE) by default, except as noted below.

- Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)
