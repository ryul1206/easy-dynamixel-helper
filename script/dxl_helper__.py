#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dynamixel_sdk as dxlsdk
import json
from getch import exit_with_getch, ask_continue_getch


class DxlHelper:
    def __init__(self, preset_path):
        preset = json.load(open(preset_path, 'r'))
        ct_folder = "../config/control_table/"

        # This is the number of connections.
        # If you use ttyUSB0 and ttyUSB1, num_port is 2.
        num_port = len(preset)

        self.port_handler_list = [
            dxlsdk.PortHandler(preset[i]['device'])
            for i in range(num_port)]

        # The 'PacketHandler' requires 'protocol version' for initialization.
        self.packet_handler_list = [
            dxlsdk.PacketHandler(preset[x]['protocol version'])
            for i in range(num_port)]

        # Open port
        for i in range(num_port):
            port_name = preset[i]['device']
            if self.port_handler_list[i].openPort():
                print("Succeeded to open the port: " + port_name)
            else:
                exit_with_getch("Failed to open the port" + port_name)

            # Dynamixel default baudrate : 57600
            if self.port_handler_list[i].setBaudRate(preset[i]['baudrate']):
                print("Succeeded to change the baudrate" + port_name)
            else:
                exit_with_getch("Failed to change the baudrate" + port_name)

# TODO d from this
# test
# ============================================

        # The key of motor_set is the ID of the motor.
        motor_set = {}
        motor = preset[0]['motors'][0]
        addr = json.load(open(ct_folder+motor['model']+".json", 'r'))

# ============================================

    def __del__(self):
        # Close port
        for port_handle in self.port_handler_list:
            port_handle.closePort()

    def _is_success(self, dxl_result, dxl_error):
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            return False
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            return False
        else:
            return True

    def enable_torque(self, motor_id):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, motor_id, addr['ram']['torque enable'], 1)
        return self._is_success(dxl_comm_result, dxl_error)

    def disable_torque(self, motor_id):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, motor_id, addr['ram']['torque enable'], 0)
        return self._is_success(dxl_comm_result, dxl_error)

    def set_goal_position(self, dxl_unit):
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
            portHandler, motor['id'], addr['ram']['goal position'], dxl_unit)
        return self._is_success(dxl_comm_result, dxl_error)

    def get_present_position(self):
        position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(
            portHandler, motor['id'], addr['ram']['present position'])
        return self._is_success(dxl_comm_result, dxl_error), position


if __name__ == "__main__":
    # Move in a sine motion with 180 degrees of amplitude
    helper = DxlHelper("../config/preset/ex_2port_4motor.json")

    motor_id = 1

    # Enable Dynamixel Torque
    if helper.enable_torque(motor_id):
        print("Dynamixel has been successfully connected")

    while 1:
        ask_continue_getch()

        # Write goal position
        dxl_goal_position = [10, 4000]
        helper.set_goal_position(dxl_goal_position[index])

        while 1:
            # Read present position
            result, dxl_present_position = helper.get_present_position()
            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" %
                  (motor_id, dxl_goal_position[index], dxl_present_position))

            # Dynamixel moving status threshold
            if not abs(dxl_goal_position[index] - dxl_present_position) > 20:
                break

        # Change goal position
        if index == 0:
            index = 1
        else:
            index = 0

    # Disable Dynamixel Torque
    helper.disable_torque(motor_id)
