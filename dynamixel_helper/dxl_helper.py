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

        self.port_handlers = []
        for port in preset:
            # Port handle
            pth = dxlsdk.PortHandler(port['device'])
            # Open port
            if pth.openPort():
                print("Succeeded to open the port: \t\t" + port['device'])
            else:
                getch_exit("Failed to open the port: \t\t" + port['device'])
            # Set baudrate
            if pth.setBaudRate(port['baudrate']):
                print("Succeeded to change the baudrate: \t" + port['device'])
            else:
                getch_exit("Failed to change the baudrate: \t" + port['device'])
            # Append
            self.port_handlers.append(pth)

        ############################################
        #             Packet Handlers
        ############################################
        # The 'PacketHandler' requires 'protocol version' for initialization.
        # KEY: 'protocol version', VALUE: 'packet_handler'

        # Duplicate cleaning
        protocol_set = set([port['protocol version'] for port in preset])
        self.packet_handlers = {
            version: dxlsdk.PacketHandler(version)
            for version in protocol_set
        }

        ############################################
        #                 Motor
        ############################################

        # Motor List
        idset = set()
        alset = set()
        motorList = []
        for portIndex, port in enumerate(preset):
            for motor in port['motors']:
                # ID Validation
                try:
                    if not isinstance(motor['id'], int):
                        getch_exit("[FATAL] Motor_ID must be type Int. Motor ID: {}".format(motor['id']))
                    elif motor['id'] in idset:
                        getch_exit("[FATAL] Duplicate Motor_ID exists. Motor ID: {}".format(motor['id']))
                    else:
                        idset.add(motor['id'])
                except KeyError as e:
                    getch_exit("[FATAL] Motor_ID was not defined.")
                # Alias Validation
                try:
                    if not isinstance(motor['alias'], str):
                        getch_exit("[ERROR] Alias must be type Str. Alias: {}".format(motor['alias']))
                    if motor['alias']:
                        if motor['alias'] in alset:
                            getch_exit("[ERROR] Duplicate Alias exists. Alias: {}".format(motor['alias']))
                        else:
                            alset.add(motor['alias'])
                    else:
                        motor['alias'] = None
                except KeyError as e:
                    motor.update({'alias': None})
                # Reconstruct motor list
                motor.update({
                    'port': portIndex,
                    'protocol version': port['protocol version']
                })
                motorList.append(motor)
                # {
                #     "id": 1,
                #     "alias": "joint_L1",
                #     "model": "XM430-W210",
                #     "port": portIndex
                #     "protocol version": 2
                # }

        # KEY: 'robotID' or 'alias', VALUE: 'DxlMotor'
        self.__motors = {}
        for motor in motorList:
            motorInstance = DxlMotor(
                motor['id'],
                motor['alias'],
                motor['model'],
                self.port_handlers[motor['port']],
                self.packet_handlers[motor['protocol version']]
            )
            self.__motors[motor['id']] = motorInstance
            if motor['alias']:
                self.__motors[motor['alias']] = motorInstance

        print("All the motor settings are complete!")
        print("You have {} motor(s).".format(len(motorList)))

    def __del__(self):
        for port in self.port_handlers:
            port.closePort()

    def get_motor(self, _id):
        return self.__motors[_id]
