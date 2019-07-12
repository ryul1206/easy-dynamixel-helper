#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dxl_helper import DxlHelper

helper = DxlHelper("example_0.json")

motor_id = 0
motor = helper.get_motor(motor_id)

print("--------------------")
motor.set_torque(True)
# dxl_unit, _ = motor.get_present_position()
# print(motor.set_goal_position((dxl_unit + 1000)%4096))
# motor.set_torque(False)
print("--------------------")
