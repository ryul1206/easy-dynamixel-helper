#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dynamixel_helper import DxlHelper


helper = DxlHelper("preset/example_0.json")

motor_id = 0
boundaries = [1500, 2500]

motor = helper.get_motor(motor_id)
motor.set_torque(True)

print("--------------------")
count = 0
while count < 5:
    print("\nLoop {}".format(count))

    goal = boundaries[count % 2]
    motor.set_goal_position(goal)

    while True:
        # Read present position
        position, result = motor.get_present_position()
        print("[ID:%03d]  GoalPos:%03d  PresPos:%03d" %
              (motor_id, goal, position))
        # Threshold
        if abs(goal - position) < 20:
            break

    # Change goal position
    count += 1

# Disable Dynamixel Torque
motor.set_torque(False)
print("--------------------")
print("Example code was finished.\n")
