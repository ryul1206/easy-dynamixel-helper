#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# base_dir = os.path.dirname(os.path.abspath(__file__))
activate_this = os.path.expanduser(
    '~/virtualenv/dxlhelper_py2test/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from dxl_motor import DxlMotor
from byteify import byteify
import constant
import dynamixel_sdk as dxlsdk
import json


# from .dxl_motor import DxlMotor
# from .byteify import byteify

# SDK Manual
# http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/api_reference/python/python_porthandler/#python

"""dddd"""


class DxlHelper(object):
    """
    testtest
    """

    def __init__(self, preset_file, verbosity='minimal'):
        # Verbose
        constant.assert_verbosity(verbosity)
        self.verbosity = constant.verbose_level[verbosity]

        # Load preset
        with open(preset_file, 'r') as f:
            preset = json.load(f, object_hook=byteify)

        ############################################
        #              Port Handlers
        ############################################
        # The 'PortHandler' requires 'device name' for initialization.
        # And the device name is different for each OS.
        #     windows: "COM1"
        #     linux: "/dev/ttyUSB0"
        #     mac: "/dev/tty.usbserial-*"

        # "/dev/ttyUSB0": PortHandler
        self.port_handlers = {}

        for port in preset["ports"]:
            name = port['device']
            self.__type_dup_check('Preset Port', name, str, self.port_handlers)
            pth = dxlsdk.PortHandler(name)
            # Open port
            if pth.openPort():
                if self.verbosity >= constant.verbose_level['detailed']:
                    print("Helper: \"{}\" Succeeded to open the port.".format(
                        name))
            else:
                print("Helper: [ERROR]")
                print("        Failed to open the port:       " + name)
                raise RuntimeError
            # Set baudrate
            if pth.setBaudRate(port['baudrate']):
                if self.verbosity >= constant.verbose_level['detailed']:
                    print("Helper: \"{}\" Succeeded to set the baudrate: {}".format(
                        name, port['baudrate']))
            else:
                print("Helper: [ERROR]")
                print("        Failed to change the baudrate: " + name)
                raise RuntimeError
            # Append
            self.port_handlers[name] = pth

        ############################################
        #             Packet Handlers
        ############################################
        # The 'PacketHandler' requires 'protocol version' for initialization.
        # KEY: 'protocol version', VALUE: 'packet_handler'

        # Duplicate cleaning
        protocol_set = set(
            [port['protocol version'] for port in preset["ports"]])
        self.packet_handlers = {
            version: dxlsdk.PacketHandler(version) for version in protocol_set}

        ############################################
        #                 Motor
        ############################################

        # Motor List
        id_set = set()
        alias_set = set()
        motor_list = []
        for motor in preset['motors']:
            # ID Validation
            try:
                self.__type_dup_check('Motor ID', motor['id'], int, id_set)
            except KeyError:
                print("Helper: [ERROR]")
                print("        Some motors have no ID.")
                print("        Please check again: " + preset_file)
                raise RuntimeError
            else:
                id_set.add(motor['id'])
            # Alias Validation
            try:
                # TODO check alias when empty in json. Is None value correctly inside?
                if motor['alias']:
                    self.__type_dup_check(
                        'Motor Alias', motor['alias'], str, alias_set)
                    alias_set.add(motor['alias'])
                else:
                    motor['alias'] = None
            except KeyError:
                motor.update({'alias': None})
            # Clean list
            motor_list.append(motor)
            # {
            #     "id": 1,
            #     "alias": "joint_L1",
            #     "model": "XM430-W210"
            # }
        self.num_motors = len(motor_list)

        # KEY: 'robotID' or 'alias', VALUE: 'DxlMotor'
        self.__motors = {}
        logging = {'O': [], 'X': []}
        for motor in motor_list:
            motor_log = (motor['id'], motor['alias'], motor['model'])
            try:
                motorInstance = DxlMotor(
                    motor['id'], motor['alias'], motor['model'],
                    self.port_handlers, self.packet_handlers,
                    verbosity=verbosity)
            except RuntimeError:
                logging['X'].append(motor_log)
                if self.verbosity >= constant.verbose_level['detailed']:
                    print("Helper: One motor setup was skipped.")
            else:
                logging['O'].append(motor_log)
                self.__motors[motor['id']] = motorInstance
                if motor['alias']:
                    self.__motors[motor['alias']] = motorInstance
                if self.verbosity >= constant.verbose_level['detailed']:
                    print("Helper: One motor setup was completed.")

        ############################################
        #                 Log
        ############################################

        if self.verbosity >= constant.verbose_level['minimal']:
            print("Helper: All motor setups have been completed.")
            print("        Success: {} motor(s) / Fail: {} motor(s)".format(
                len(logging['O']), len(logging['X'])))
            for ox, logs in logging.items():
                logs.sort()
                for log in logs:
                    print("          ({}) id: {}, alias: {}, model: {}".format(
                        ox, log[0], log[1], log[2]))

    def __del__(self):
        for port in self.port_handlers.values():
            port.closePort()

    @staticmethod
    def __type_dup_check(name, value, expected_type, list_like):
        if not isinstance(value, expected_type):
            print("Helper: [ERROR]")
            print("        {} must be \'{}\', not \'{}\'. Value: {}".format(
                name, expected_type.__name__, type(value).__name__, value))
            raise TypeError
        elif value in list_like:
            print("Helper: [ERROR]")
            print("        Duplicate {} detected. Value: {}".format(
                name, value))
            raise ValueError

    def get_motor(self, _id):
        return self.__motors[_id]


if __name__ == "__main__":

    d = DxlHelper("asdfasdfasdf.json")

    print("--------------------")
    motor_id = 0
    motor = d.get_motor(motor_id)

    motor.set_torque(True)
    dxl_unit, _ = motor.get_present_position()
    print(motor.set_goal_position((dxl_unit + 2048) % 4096))
