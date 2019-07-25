#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SDK Manual
# http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/api_reference/python/python_porthandler/#python

import dynamixel_sdk as dxlsdk
import json
from .dxl_motor import DxlMotor
from .byteify import byteify
from .getch import getch_exit, getch_ask


class DxlHelper(object):
    def __init__(self, preset_file):
        # Load preset
        try:
            with open(preset_file, 'r') as f:
                preset = json.load(f, object_hook=byteify)
        except FileNotFoundError as e:
            getch_exit(e)

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
                print("Succeeded to open the port: \t\t" + name)
            else:
                getch_exit("[ERROR] Failed to open the port: \t\t" + name)
            # Set baudrate
            if pth.setBaudRate(port['baudrate']):
                print("Succeeded to change the baudrate: \t" + name)
            else:
                getch_exit("[ERROR] Failed to change the baudrate: \t" + name)
            # Append
            self.port_handlers[name] = pth

        ############################################
        #             Packet Handlers
        ############################################
        # The 'PacketHandler' requires 'protocol version' for initialization.
        # KEY: 'protocol version', VALUE: 'packet_handler'

        # Duplicate cleaning
        protocol_set = set([port['protocol version'] for port in preset["ports"]])
        self.packet_handlers = {
            version: dxlsdk.PacketHandler(version) for version in protocol_set
        }

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
            except KeyError as e:
                getch_exit("[FATAL] Motor_ID was not defined.")
            id_set.add(motor['id'])
            # Alias Validation
            try:
                if motor['alias']:
                    self.__type_dup_check(
                        'Motor Alias', motor['alias'], str, alias_set)
                    alias_set.add(motor['alias'])
                else:
                    motor['alias'] = None
            except KeyError as e:
                motor.update({'alias': None})
            # Clean list
            motor_list.append(motor)
            # {
            #     "id": 1,
            #     "alias": "joint_L1",
            #     "model": "XM430-W210"
            # }

        # KEY: 'robotID' or 'alias', VALUE: 'DxlMotor'
        self.__motors = {}
        for motor in motor_list:
            motorInstance = DxlMotor(
                motor['id'], motor['alias'], motor['model'],
                self.port_handlers, self.packet_handlers)
            self.__motors[motor['id']] = motorInstance
            if motor['alias']:
                self.__motors[motor['alias']] = motorInstance

        print("All the motor settings are complete!")
        print("You have {} motor(s).".format(len(motor_list)))

    def __del__(self):
        for port in self.port_handlers:
            port.closePort()

    @staticmethod
    def __type_dup_check(name, value, expected_type, list_like):
        fail_msg = ""
        level = 'ERROR'
        if not isinstance(value, expected_type):
            fail_msg = "[{}] {} must be type {}. But: {}".format(
                level, name, expected_type.__name__, value)
        elif value in list_like:
            fail_msg = "[{}] Duplicate value exists. {}: {}".format(
                level, name, value)
        if fail_msg:
            getch_exit(fail_msg)

    def get_motor(self, _id):
        return self.__motors[_id]
