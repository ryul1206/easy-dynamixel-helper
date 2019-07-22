#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import dynamixel_sdk as dxlsdk
import json
from .byteify import byteify
from .getch import getch_exit, getch_ask


class DxlMotor(object):
    def __init__(self, _id, alias, model, port_handler, packet_handler):
        self.id = _id
        self.port_handler = port_handler
        self.packet_handler = packet_handler

        # Load control tables
        pkg_directory = os.path.dirname(os.path.abspath(__file__))
        control_table_path = pkg_directory + "/config/"
        control_table_file = control_table_path + model + ".json"
        try:
            with open(control_table_file, 'r') as f:
                control_table = json.load(f, object_hook=byteify)
        except FileNotFoundError as e:
            getch_exit(e)
        self.EEPROM = control_table['eeprom']
        self.RAM = control_table['ram']

    def __eq__(self, other):
        return self.id == other.id

    def _is_success(self, dxl_result, dxl_error):
        if dxl_result != dxlsdk.COMM_SUCCESS:
            print(self.packet_handler.getTxRxResult(dxl_result))
            return False
        elif dxl_error != 0:
            print(self.packet_handler.getRxPacketError(dxl_error))
            return False
        return True

    def set_torque(self, enable):
        dxl_result, dxl_error = self.packet_handler.write1ByteTxRx(
            self.port_handler, self.id, self.RAM['torque enable'],
            1 if enable else 0)
        return self._is_success(dxl_result, dxl_error)

    def set_goal_position(self, dxl_unit):
        dxl_result, dxl_error = self.packet_handler.write4ByteTxRx(
            self.port_handler, self.id, self.RAM['goal position'],
            dxl_unit)
        return self._is_success(dxl_result, dxl_error)

    def get_present_position(self):
        position, dxl_result, dxl_error = self.packet_handler.read4ByteTxRx(
            self.port_handler, self.id, self.RAM['present position'])
        return position, self._is_success(dxl_result, dxl_error)
