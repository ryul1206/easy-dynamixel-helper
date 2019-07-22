#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from dynamixel_helper import DxlHelper

current_dir = os.path.dirname(os.path.abspath(__file__))

helper = DxlHelper(current_dir + "/preset/1motor_1port.json")

motor_id = 0
motor = helper.get_motor(motor_id)

print("--------------------")
motor.set_torque(True)
dxl_unit, _ = motor.get_present_position()
print(motor.set_goal_position((dxl_unit + 2048) % 4096))
print("--------------------")
