#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dynamixel_helper import DxlHelper


def msg(motor_id, goal, position):
    return "[ID:%03d]  GoalPos:%03d  PresPos:%03d" % (motor_id, goal, position)


helper = DxlHelper("preset/example_2.json")

boundaries = [1500, 2500]
position = [0, 0]

number = 2
motors = [helper.get_motor(i) for i in range(number)]

motors[0].set_torque(True)
motors[1].set_torque(True)

print("--------------------")
count = 0
while count < 5:
    print("\nLoop {}".format(count))
    goal = boundaries[count % 2]

    motors[0].set_goal_position(goal)
    motors[1].set_goal_position(goal)

    while True:
        # Read present position
        position[0], _ = motors[0].get_present_position()
        position[1], _ = motors[1].get_present_position()
        print(msg(0, goal, position[0]) + "\t" + msg(1, goal, position[1]))
        # Threshold
        if (abs(goal - position[0]) < 20) and (abs(goal - position[1]) < 20):
            break

    # Change goal position
    count += 1

# Disable Dynamixel Torque
motors[0].set_torque(False)
motors[1].set_torque(False)
print("--------------------")
print("Example code was finished.\n")
