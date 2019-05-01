#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dynamixel_sdk as dxlsdk
from getch import getch


class DxlHelper:
    def __init__(self, preset_name):


        ################################################33        
        # Control table address
        # Control table address is different in Dynamixel model
        ADDR_PRO_TORQUE_ENABLE = 64
        ADDR_PRO_GOAL_POSITION = 116
        ADDR_PRO_PRESENT_POSITION = 132
        #########################
        # Protocol version
        # See which protocol version is used in the Dynamixel
        PROTOCOL_VERSION = 2.0

        # Default setting
        DXL_ID = 1                 # Dynamixel ID : 1
        BAUDRATE = 57600             # Dynamixel default baudrate : 57600
        DEVICENAME = '/dev/ttyUSB0'    # Check which port is being used on your controller
        # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

        TORQUE_ENABLE = 1                 # Value for enabling the torque
        TORQUE_DISABLE = 0                 # Value for disabling the torque
        # Dynamixel will rotate between this value
        DXL_MINIMUM_POSITION_VALUE = 10
        # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
        DXL_MAXIMUM_POSITION_VALUE = 4000
        # Dynamixel moving status threshold
        DXL_MOVING_STATUS_THRESHOLD = 20

        index = 0
        dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE,
                            DXL_MAXIMUM_POSITION_VALUE]         # Goal position

        # Initialize PortHandler instance
        # Set the port path
        # Get methods and members of PortHandlerLinux or PortHandlerWindows
        portHandler = PortHandler('/dev/ttyUSB0')

        # Initialize PacketHandler instance
        # Set the protocol version
        # Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
        packetHandler = PacketHandler(PROTOCOL_VERSION)

        # Open port
        if portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()


        # Set port baudrate
        if portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
            quit()


