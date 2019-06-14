#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dxl_helper
from getch import getch_exit, getch_ask


# Example code
helper = dxl_helper.DxlHelper("../config/preset/example_2port_4motor.json")

# Enable Dynamixel torque
motor_id = 1
goals = [10, 4000]
index = 0

if helper.set_torque(motor_id, True):
    print("Successfully connected: Dynamixel ID {}".format(motor_id))

count = 0
while count < 10:
    print("Loop {}".format(count))
    getch_ask()

    helper.set_goal_position(index)

    while True:
        # Read present position
        position, result = helper.get_present_position()
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" %
              (motor_id, goals[index], position))
        # Threshold
        if not abs(goals[index] - position) > 20:
            break

    # Change goal position
    index = (index + 1) % 2

# Disable Dynamixel Torque
helper.set_torque(motor_id, False)
getch_exit("Example code was finished.")
