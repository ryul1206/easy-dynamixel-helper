# Easy Dynamixel Helper

This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.

1. [Dependencies](#dependencies)
   1. [1. Python Environment](#1-python-environment)
      1. [Dynamixel SDK Setup](#dynamixel-sdk-setup)
2. [About The Licenses](#about-the-licenses)
3. [TODO](#todo)

## Dependencies

### 1. Python Environment

#### [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) Setup

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

## About The Licenses

The contents of this repository are subject to the MIT license by default, except as noted below.

1. Dynamixel SDK is under the [Apache-2.0](https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/LICENSE)
   <!-- 1. `dxl_helper.py` is modified from `read_write.py` of `${DynamixelSDK}/python/...` -->

## TODO

- [ ] Prototype
- [ ] Update Readme
- [ ] C++
