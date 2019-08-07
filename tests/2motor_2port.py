#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
# base_dir = os.path.dirname(os.path.abspath(__file__))
activate_this = os.path.expanduser(
    '~/virtualenv/dxlhelper_py2test/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# import os
from dynamixel_helper import DxlHelper

# current_dir = os.path.dirname(os.path.abspath(__file__))
# helper = DxlHelper(current_dir + "/preset/2motor_2port.json", verbosity='detailed')

helper = DxlHelper("auto.json")
# helper = DxlHelper("auto.json", verbosity='detailed')


motor = helper.get_motor('joint_1')


motor.set_torque(False)
motor.set_operating_mode(3)  # position mode
motor.set_torque(True)
dxl_unit, _ = motor.get_present_position()

v = 1000
print(motor.set_goal_position((dxl_unit + v) % 4096))


motor.set_torque(False)
motor.set_operating_mode(1)  # velocity mode
motor.set_torque(True)

motor.set_goal_velocity(-30)
time.sleep(3)
motor.set_goal_velocity(30)
time.sleep(3)
motor.set_goal_velocity(-30)
time.sleep(3)

# clean up
motor = helper.get_motor('joint_0')
motor.set_torque(False)
motor.set_operating_mode(3)  # position mode
motor.set_torque(True)

motor = helper.get_motor('joint_1')
motor.set_torque(False)
motor.set_operating_mode(3)  # position mode
motor.set_torque(True)
