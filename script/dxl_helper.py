#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dynamixel_sdk as dxlsdk
import json
from getch import getch_exit, getch_ask
import random
import string


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


class DxlHelper:
    def __init__(self, preset_file):
        # Load preset
        preset = json.load(open(preset_file, 'r'))

        ############################################
        #                  Port
        ############################################
        # The number of connections (ports)
        # If you use 2 ports, ttyUSB0 and ttyUSB1, num_port == 2.
        num_port = len(preset)

        # The 'PortHandler' requires 'device name' for initialization.
        # And the device name is different for each OS.
        #     windows: "COM1"
        #     linux: "/dev/ttyUSB0"
        #     mac: "/dev/tty.usbserial-*"
        self.port_handlers = [dxlsdk.PortHandler(
            preset[i]['device']) for i in range(num_port)]

        # The 'PacketHandler' requires 'protocol version' for initialization.
        self.packet_handlers = [dxlsdk.PacketHandler(
            preset[i]['protocol_version']) for i in range(num_port)]

        for i in range(num_port):
            name = preset[i]['device']
            # Open port
            if self.port_handlers[i].openPort():
                print("Succeeded to open the port: " + name)
            else:
                getch_exit("Failed to open the port: " + name)
            # Set baudrate
            if self.port_handlers[i].setBaudRate(preset[i]['baudrate']):
                print("Succeeded to change the baudrate: " + name)
            else:
                getch_exit("Failed to change the baudrate: " + name)

        ############################################
        #                 Motor
        ############################################
        self.motors_alias = {}
        self.motors_id = {}
        for port_idx in range(num_port):
            for m in preset[port_idx]['motors']:
                motor = {'alias': str(m['alias']),
                         'model': str(m['model']),
                         'id': int(m['id'])}
                # Empty alias
                if len(motor['alias']) == 0:
                    motor['alias'] = random_string()
                # Alias
                if motor['alias'] in self.motors_alias:
                    getch_exit("[Error] Duplicate Motor Alias Exists")
                else:
                    self.motors_alias[motor['alias']] = motor
                # ID
                if motor['id'] in self.motors_id:
                    getch_exit("[Error] Duplicate Motor ID Exists")
                else:
                    self.motors_id[motor['id']] = motor

        # Check that the control table exists
        ctable_path = "../config/control_table/"
        self.ctables = {}
        for key in self.motors_id:
            model = self.motors_id[key]['model']
            ctable = json.load(open(ctable_path + model + ".json", 'r'))
            # TODO store ctable into self.ctables
            # TODO check the ctable exist and ifnot exit

        print("Succeeded to read the motor config! \
            You have {} motor(s).".format(len(self.motors_id)))

    def __del__(self):
        # Close ports
        for port in self.port_handlers:
            port.closePort()

    def _is_success(self, packet_handle_idx as idx, dxl_result, dxl_error):
        if dxl_result != dxlsdk.COMM_SUCCESS:
            print(self.packet_handlers[idx].getTxRxResult(dxl_result))
            return False
        elif dxl_error != 0:
            print(self.packet_handlers[idx].getRxPacketError(dxl_error))
            return False
        else:
            return True

    # TODO enable torque methods

if __name__ == "__main__":
    # Example code
    helper = DxlHelper("../config/preset/ex_1port_1motor.json")

    # Enable Dynamixel torque
    motor_id = 1
    if helper.enable_torque(motor_id):
        print("Successfully connected: Dynamixel ID {}".format(motor_id))
