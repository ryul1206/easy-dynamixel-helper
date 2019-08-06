#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
from dynamixel_helper import DxlHelper

# current_dir = os.path.dirname(os.path.abspath(__file__))
# helper = DxlHelper(current_dir + "/preset/2motor_2port.json", verbosity='detailed')
helper = DxlHelper("2motor_2port.json", verbosity='detailed')


def move(id_, v):
    motor = helper.get_motor(id_)
    motor.set_torque(True)
    dxl_unit, _ = motor.get_present_position()
    print(motor.set_goal_position((dxl_unit + v) % 4096))

print("--------------------")
move(0, 500)
print("--------------------")
move(1, 2000)
