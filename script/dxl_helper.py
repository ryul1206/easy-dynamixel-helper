#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dynamixel_sdk as dxlsdk
import json
from getch import exit_with_getch, ask_continue


class DxlHelper:
    def __init__(self, preset_path):
        preset = json.load(open(preset_path, 'r'))
        ct_folder = "../config/control_table/"
        motor = preset[0]['motors'][0]
        addr = json.load(open(ct_folder+motor['model']+".json", 'r'))
        
        # Device Names by OS
        # Windows: "COM1"
        # Linux: "/dev/ttyUSB0"
        # Mac: "/dev/tty.usbserial-*"

        # Initialize PortHandler instance
        # Get methods and members of PortHandlerLinux or PortHandlerWindows
        portHandler = dxlsdk.PortHandler(preset[0]['device'])

        # Initialize PacketHandler instance
        # Get Protocol1PacketHandler or Protocol2PacketHandler
        packetHandler = dxlsdk.PacketHandler(preset[0]['protocol version'])

        # Open port
        if portHandler.openPort():
            print("Succeeded to open the port")
        else:
            exit_with_getch("Failed to open the port")

        # Dynamixel default baudrate : 57600
        if portHandler.setBaudRate(preset[0]['baudrate']):
            print("Succeeded to change the baudrate")
        else:
            exit_with_getch("Failed to change the baudrate")

        
        # Enable Dynamixel Torque
        TORQUE_ENABLE = 1                 # Value for enabling the torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, motor['id'], addr['ram']['torque enable'], TORQUE_ENABLE)

        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel has been successfully connected")

        while 1:
            ask_continue()

            dxl_goal_position = [10, 4000]         # Goal position

            # Write goal position
            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
                portHandler, motor['id'], addr['ram']['goal position'], dxl_goal_position[index])
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            while 1:
                # Read present position
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(
                    portHandler, motor['id'], addr['ram']['present position'])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

                print("[ID:%03d] GoalPos:%03d  PresPos:%03d" %
                      (motor['id'], dxl_goal_position[index], dxl_present_position))

                # Dynamixel moving status threshold
                threshold = 20
                if not abs(dxl_goal_position[index] - dxl_present_position) > threshold:
                    break

            # # Change goal position
            # if index == 0:
            #     index = 1
            # else:
            #     index = 0

        # Disable Dynamixel Torque
        TORQUE_DISABLE = 0                 # Value for disabling the torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, motor['id'], addr['ram']['torque enable'], TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        # Close port
        portHandler.closePort()


if __name__ == "__main__":
    # Move in a sine motion with 180 degrees of amplitude
    helper = DxlHelper("../config/preset/example_1p1m.json")
