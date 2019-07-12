#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dxl_helper import DxlHelper
import os

print( os.getcwd())

helper = DxlHelper("example_0.json")

motor_id = 0
motor = helper.get_motor(motor_id)

print("--------------------")
print(motor.set_torque(True))
print("--------------------")
