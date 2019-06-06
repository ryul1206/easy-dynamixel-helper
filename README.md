# Easy Dynamixel Helper

![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/easy-dynamixel-helper.svg)

This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.

**[Warning]** Currently, this helper has not been tested. But you can use this if you want. Feedback is always welcome.

1. [Setup](#setup)
   1. [For Python](#for-python)
      1. [Dynamixel SDK Installation](#dynamixel-sdk-installation)
      2. [Dynamixel Helper](#dynamixel-helper)
2. [Usage](#usage)
3. [Licenses](#licenses)
4. [TODO](#todo)

## Setup

### For Python

Python 2.x or Python 3.x

#### [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) Installation

1. Clone the official SDK repository into your folder, for example, `~/lib`.

   ```bash
   git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
   ```

2. Go into a `python` folder of your cloned SDK.

   ```bash
   cd ${your_path}/DynamixelSDK/python
   ```

3. Run `setup.py` as administrator to install the library.

   ```bash
   sudo python setup.py install
   ```

#### Dynamixel Helper

1. clone this helper to your project folder

## Usage

Sorry... Currently, only 'example.py' is provided. A detailed description will be updated later.

## Licenses

The contents of this repository are subject to the MIT license by default, except as noted below.

- Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)
   <!-- 1. `dxl_helper.py` is modified from `read_write.py` of `${DynamixelSDK}/python/...` -->

## TODO

- Verify actual motor driving
- Update a detailed tutorial
- Wrapping more features of the SDK
- C++
- Korean readme
