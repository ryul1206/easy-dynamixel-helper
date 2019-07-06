#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SDK Manual
# http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/api_reference/python/python_porthandler/#python

from getch import getch_exit, getch_ask
import dynamixel_sdk as dxlsdk
# import random
import string
import copy
import json

# TODO: test history

# TODO: Is byteify also return some Int?

# TODO: Comment python description for all functions [link](https://www.python.org/dev/peps/pep-0257/)

# TODO: Test in both Python 2.x and Python 3.x

# TODO: Verify actual motor driving

# TODO: Wrapping more features of the SDK

# TODO: Verify control table (key, addr, and etc.)


# def random_string(string_length=10):
#     """Generate a random string of fixed length."""
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(string_length))


def byteify(unicode_json):
    # Thanks to Mark Amery from StackOverflow.
    # https://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-from-json
    if isinstance(unicode_json, dict):
        return {byteify(key): byteify(value)
                for key, value in unicode_json.iteritems()}
    elif isinstance(unicode_json, list):
        return [byteify(element) for element in unicode_json]
    elif isinstance(unicode_json, unicode):
        return unicode_json.encode('utf-8')
    return unicode_json


class DxlHelper:
    class AliasedKey:
        def __init__(self, key, alias):
            self.key = key
            self.alias = alias

        def __eq__(self, other):
            return other is self.key or other is self.alias

    def __init__(self, preset_file):
        # Load preset
        preset = json.load(open(preset_file, 'r'), object_hook=byteify)

        # The number of connections (ports)
        # If you use 2 ports, ttyUSB0 and ttyUSB1, num_port == 2.
        num_port = len(preset)

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
                print("Succeeded to open the port: " + port['device'])
            else:
                getch_exit("Failed to open the port: " + port['device'])
            # Set baudrate
            if pth.setBaudRate(port['baudrate']):
                print("Succeeded to change the baudrate: " + name)
            else:
                getch_exit("Failed to change the baudrate: " + name)
            # Append
            self.port_handlers.append(pth)

        ############################################
        #             Packet Handlers
        ############################################
        # The 'PacketHandler' requires 'protocol version' for initialization.
        # KEY: 'protocol_version', VALUE: 'packet_handler'

        # Duplicate cleaning
        protocol_set = set([port['protocol_version'] for port in preset])
        self.packet_handlers = {
            version: dxlsdk.PacketHandler(version)
            for version in protocol_set
        }

        ############################################
        #                 Motor
        ############################################
        # KEY: 'robotID' or 'alias', VALUE: 'DxlMotor'

        # Motor List
        idset = set()
        alset = set()
        for motor in (port['motors'] for port in preset):
            # ID Validation
            try:
                if not isinstance(motor['id'], int):
                    getch_exit("[FATAL] Motor_ID must be type Int.")
                elif motor['id'] in idset:
                    getch_exit("[FATAL] Duplicate Motor_ID exists.")
                else:
                    idset.add(motor['id'])
            except KeyError as e:
                getch_exit("[FATAL] Motor_ID was not defined.")
            # Alias Validation
            try:
                if not isinstance(motor['alias'], str):
                    getch_exit("[ERROR] Alias must be type Str.")
                elif motor['alias'] in alset:
                    getch_exit("[ERROR] Duplicate Alias exists.")
                else:
                    alset.add(motor['alias'])
            except KeyError as e:
                pass
            else:
                pass


        # ID Validation
        for motorList
        idList = []
        for port in preset:
            for motor in port['motors']:
                if 
                if motor['id'] not in idList:
                    idList.append(motor['id'])
                else:
                    getch_exit("[Error] Duplicate Motor Alias Exists")
        
        # Alias
        self.motors = {}

        for portIndex, port in enumerate(preset):
            for m in port['motors']:
                motor = copy.deepcopy(m)
                motor.update({'port': portIndex})
                # {
                #     "id": 1,
                #     "alias": "joint_L1",
                #     "model": "XM430-W210",
                #     "port": portIndex
                # }



                # Empty alias
                if not motor['alias']:
                    motor['alias'] = random_string()
                key = self.AliasedKey(motor['id'], motor['alias'])

                # Duplicate Alias rejection
                if motor['alias'] in self.motors:
                    getch_exit("[Error] Duplicate Motor Alias Exists")
                # Duplicate ID rejection\
                elif motor['id'] in self.motors_id:
                    getch_exit("[Error] Duplicate Motor ID Exists")
                else:
                    self.motors[key] = motor

        # Load control tables
        ctable_path = "../config/"
        self.ctables = {}
        for motoer_key, motor in self.motors:
            model = self.motor['model']
            # Check that already loaded
            if model in self.ctables:
                continue
            # Check that the file exists
            ctable_file = ctable_path + model + ".json"
            ctable = json.load(open(ctable_file, 'r'), object_hook=byteify)
            self.ctables[model] = ctable

        print("Succeeded to read the motor config! \
            You have {} motor(s).".format(len(self.motors_id)))

    def __del__(self):
        for port in self.port_handlers:
            port.closePort()

    @staticmethod
    def _is_success(packet_handler, dxl_result, dxl_error):
        if dxl_result != dxlsdk.COMM_SUCCESS:
            print(packet_handler.getTxRxResult(dxl_result))
            return False
        elif dxl_error != 0:
            print(packet_handler.getRxPacketError(dxl_error))
            return False
        return True

    def _find_four(self, alias_or_id):
        # TODO : We don't need to find four, everytime.
        #        Change to only once.
        motor = self.motors[alias_or_id]
        addr = self.ctables[mtr['model']]
        porthd = self.port_handlers[mtr['port']]
        packethd = self.packet_handlers[mtr['port']]
        return motor['id'], addr, porthd, packethd

    def set_torque(self, alias_or_id, enable):
        motorID, addr, porthd, packethd = self._find_four(alias_or_id)
        dxl_result, dxl_error = packethd.write1ByteTxRx(
            porthd, motorID, addr['ram']['torque enable'], 1 if enable else 0)
        return self._is_success(packethd, dxl_result, dxl_error)

    def set_goal_position(self, alias_or_id, dxl_unit):
        motorID, addr, porthd, packethd = self._find_four(alias_or_id)
        dxl_result, dxl_error = packethd.write4ByteTxRx(
            porthd, motorID, addr['ram']['goal position'], dxl_unit)
        return self._is_success(packethd, dxl_result, dxl_error)

    def get_present_position(self, alias_or_id):
        motorID, addr, porthd, packethd = self._find_four(alias_or_id)
        position, dxl_result, dxl_error = packethd.read4ByteTxRx(
            porthd, motorID, addr['ram']['present position'])
        return position, self._is_success(packethd, dxl_result, dxl_error)
