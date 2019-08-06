#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dynamixel_helper import DxlHelper


helper = DxlHelper("preset/example_0.json")

motor_id = 0

motor = helper.get_motor(motor_id)
motor.set_torque(True)

print("--------------------")
dxl_unit, _ = motor.get_present_position()
print(motor.set_goal_position((dxl_unit + 2048) % 4096))
print("--------------------")
