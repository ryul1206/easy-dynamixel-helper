# Easy Dynamixel Helper

![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/easy-dynamixel-helper.svg)

This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.

1. [Setup](#setup)
   1. [For Python](#for-python)
      1. [Dynamixel SDK Installation](#dynamixel-sdk-installation)
2. [Licenses](#licenses)

## Setup

### For Python

Python 2.x or Python 3.x

#### [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) Installation

1. Clone the SDK repository into your folder, for example, `~/lib`.

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

## Licenses

The contents of this repository are subject to the MIT license by default, except as noted below.

1. Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)
   <!-- 1. `dxl_helper.py` is modified from `read_write.py` of `${DynamixelSDK}/python/...` -->

<!-- ## TODO

- [ ] Prototype
- [ ] C++ -->
