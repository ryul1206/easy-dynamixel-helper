#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# base_dir = os.path.dirname(os.path.abspath(__file__))
activate_this = os.path.expanduser(
    '~/virtualenv/dxlhelper_py2test/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# import os
from dynamixel_helper import DxlHelper

# current_dir = os.path.dirname(os.path.abspath(__file__))
# helper = DxlHelper(current_dir + "/preset/2motor_2port.json", verbosity='detailed')
helper = DxlHelper("minimal.json")  #, verbosity='detailed')


def move(id_, v):
    motor = helper.get_motor(id_)
    motor.set_torque(True)
    dxl_unit, _ = motor.get_present_position()
    print(motor.set_goal_position((dxl_unit + v) % 4096))

print("--------------------")
move(0, 2000)
print("--------------------")
move(1, 2000)
