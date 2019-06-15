# Easy Dynamixel Helper

![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/easy-dynamixel-helper.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/overview/master)

TODO: a badge of pypi release version (/pypi/v/:packageName.svg)

This helper is a python wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.

**[Warning]** Currently, I have not tested this helper. (The test will be on **July**)

TODO: korean readme

TODO: update figure (direct writing on the control table)

<!-- Your code ===> DXL Helper ===> Your motor(control table) -->

1. [Getting Started](#getting-started)
   1. [Prerequisites](#prerequisites)
   2. [Installing for Python](#installing-for-python)
2. [Simple Example](#simple-example)
3. [Tutorial](#tutorial)
4. [Authors](#authors)
5. [Release Notes](#release-notes)
6. [Test Notes](#test-notes)
7. [Licenses](#licenses)

<!-- https://gist.github.com/PurpleBooth/109311bb0361f32d87a2 -->

## Getting Started

### Prerequisites

You need to install the official [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) before using this helper.

<details><summary>CLICK ME (Dynamixel SDK Installation)</summary>
<p>

1. Clone the official SDK repository into your custom folder, for example, I created `~/lib`.

    ```bash
    git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    ```

2. Go into a `/DynamixelSDK/python` folder of your cloned SDK.

    ```bash
    cd ${your_download_path}/DynamixelSDK/python
    ```

3. Run `setup.py` as administrator to install the library.

    ```bash
    sudo python setup.py install
    ```

</p>
</details>

### Installing for Python

TODO: pip install will be update

## Simple Example

TODO: one motor

## Tutorial

TODO: detail tutorial / use new markdown.

## Authors

1. **Hong-ryul Jung** - _Initial work_ - [ryul1206](https://github.com/ryul1206)
2. **Il-ho Oh** - _Initial work_

## Release Notes

TODO: release version 1.0.0

-   Apply [CodeFactor](https://www.codefactor.io/) to manage code quality

## Test Notes

TODO: test history

TODO: Is byteify also return some Int?

TODO: Comment python description for all functions [link](https://www.python.org/dev/peps/pep-0257/)

TODO: Test in both Python 2.x and Python 3.x

TODO: Verify actual motor driving

TODO: Wrapping more features of the SDK

TODO: Verify control table (key, addr, and etc.)

## Licenses

The contents of this repository are subject to the [MIT license](/LICENSE) by default, except as noted below.

-   Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)
