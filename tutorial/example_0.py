#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dxl_helper import DxlHelper
import os

print( os.getcwd())

helper = DxlHelper("./preset/example_0.json")

motor_id = 0
motor = helper.get_motor(motor_id)

print("--------------------")
print(motor.set_torque(True))
print(motor.get_present_position())
dxl_unit, _ = motor.get_present_position()
print(motor.set_goal_position((dxl_unit + 1000)%4096))
print(motor.get_present_position())
print("--------------------")
