#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from itertools import product

import dynamixel_sdk as dxlsdk
# from .byteify import byteify
import constant
from byteify import byteify


class DxlMotor(object):
    """One DxlMotor represents one motor.

    The DxlMotor directly modifies its control table.

    Attributes:
        verbosity: <int>
        id: <int>
        alias: <str>
        model: <str>
        port_handler: <dynamixel_sdk...PortHandler object>
        packet_handler: <dynamixel_sdk...PacketHandler object>
        EEPROM:
        RAM:
    """

    def __init__(self, id_, alias, model, port_handlers, packet_handlers,
                 verbosity):
        """Inits

        Args:
            id_:
            alias:
            model:
            port_handlers:
            packet_handlers:
            verbosity: 'quiet' or 'minimal' or 'detailed'
        Raises:
            RuntimeError: If the verbosity string is not in verbose_level
        """
        # Verbose
        constant.assert_verbosity(verbosity)
        self.verbosity = constant.verbose_level[verbosity]

        """
        port_handler
        packet_handler
        EEPROM
        RAM
        """
        self.id = id_
        self.alias = alias
        self.model = model

        # Load control tables
        # TODO customizable path
        control_table_path = "./config/"
        control_table_file = control_table_path + model + ".json"
        with open(control_table_file, 'r') as f:
            control_table = json.load(f, object_hook=byteify)
        self.EEPROM = control_table['eeprom']
        self.RAM = control_table['ram']
        # port_handlers['/dev/ttyUSB0']
        # packet_handlers[1.0]
        self.port_handler = None
        self.packet_handler = None
        self.__find_correct_handle(port_handlers, packet_handlers)

        if self.verbosity >= constant.verbose_level['detailed']:
            print("Helper: One motor instance was created. id: "+str(self.id))

    def __eq__(self, other):
        """"""
        return self.id == other.id

    def __find_correct_handle(self, port_handlers, packet_handlers):
        """
        """
        # ##### no error
        # packet O port O (corr_power O)
        # ##### [TxRxResult] There is no status packet!
        # packet O port O (corr_power X)
        # packet O port X (worng_power O)
        # packet O port X (worng_power X)
        # packet X port O (corr_power O)
        # packet X port O (corr_power X)
        # packet X port X (worng_power O)
        # packet X port X (worng_power X)
        success = False

        # These are intended error!
        # So, change the verbosity level to 'quiet' temporarily.
        original_verbosity = self.verbosity
        self.verbosity = constant.verbose_level['quiet']
        # Get all combinations of (port, packet) tuples
        for port, packet in product(port_handlers.values(),
                                    packet_handlers.values()):
            self.port_handler = port
            self.packet_handler = packet
            _, success = self.get_present_position()
            if success:
                break
        self.verbosity = original_verbosity
        if not success:
            print("Helper: [ERROR] ID:{}, Alias:{}, Model:{}".format(
                self.id, self.alias, self.model))
            print("        Motor connection failed.")
            print("        Please check your connection or \"[preset].json\".")
            print("        Common causes of this phenomenon like below:")
            print("          1. The power of a motor is turned off.")
            print("          2. Some port description is wrong in the JSON.")
            raise RuntimeError

    def __is_success(self, dxl_result, dxl_error):
        """
        """
        if dxl_result != dxlsdk.COMM_SUCCESS:
            # [TxRxResult] There is no status packet!
            # motor power not connected
            if self.verbosity >= constant.verbose_level['minimal']:
                print(self.packet_handler.getTxRxResult(dxl_result))
            return False
        elif dxl_error != 0:
            if self.verbosity >= constant.verbose_level['minimal']:
                print(self.packet_handler.getRxPacketError(dxl_error))
            return False
        return True

    ############################################
    #                 EEPROM
    ############################################

    ############################################
    #                 RAM
    ############################################
    def set_torque(self, enable):
        """
        """
        dxl_result, dxl_error = self.packet_handler.write1ByteTxRx(
            self.port_handler, self.id, self.RAM['torque enable'],
            1 if enable else 0)
        return self.__is_success(dxl_result, dxl_error)

    def set_goal_position(self, dxl_unit):
        """
        """
        dxl_result, dxl_error = self.packet_handler.write4ByteTxRx(
            self.port_handler, self.id, self.RAM['goal position'],
            dxl_unit)
        return self.__is_success(dxl_result, dxl_error)

    def get_present_position(self):
        """
        """
        position, dxl_result, dxl_error = self.packet_handler.read4ByteTxRx(
            self.port_handler, self.id, self.RAM['present position'])
        return position, self.__is_success(dxl_result, dxl_error)
