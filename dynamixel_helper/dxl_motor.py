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

    def __init__(self, id_, alias, model,
                 port_handlers, baud_rates,
                 packet_handlers,
                 verbosity):
        """Inits

        Args:
            id_:
            alias:
            model:
            port_handlers:
            baud_rates:
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

        # Properties
        self.port_name = ""
        self.protocol = None
        self.baud = None
        # port_handlers: {'/dev/ttyUSB0': {'handler:xx, 'baud rate':None}}
        # packet_handlers: {2.0: xx}
        self.port_handler = None
        self.packet_handler = None
        self.__find_correct_handle(port_handlers, baud_rates, packet_handlers)

        if self.verbosity >= constant.verbose_level['detailed']:
            print("Helper: One motor instance was created. id: "+str(self.id))

    def __eq__(self, other):
        """"""
        return self.id == other.id

    def __find_correct_handle(self,
                              port_handlers, baud_rates,
                              packet_handlers):
        """
        1. Get all combinations of (port, packet) tuples

        2. Find correct baud rate
           "setBaudRate()" returns True if the baud value is "possible".
           Without a motor, we don't know which value is actually matched.
        """

        # Find correct baud rate
        # found = False
        # for baud in preset['baud rates']:
        #     found = port_handler.setBaudRate(baud)
        #     print("======= ", found, baud)
        #     if found:
        #         if self.verbosity >= constant.verbose_level['detailed']:
        #             print("Helper: The baudrate of \"{}\" is {}."
        #                     .format(name, port['baudrate']))
        #         break

        # if not found:
        #     print("Helper: [ERROR] Failed to set the baudrate of \"{}\""
        #             .format(name))
        #     raise RuntimeError
        # Append
        # self.port_handlers[name] = port_handler

        # These are intended error!
        # So, change the verbosity level to 'quiet' temporarily.
        original_verbosity = self.verbosity
        # self.verbosity = constant.verbose_level['quiet']

        print("??????????")

        success = False
        # Get all cases of (port, packet) tuples
        print(cases)
        print(port_handlers)
        print(packet_handlers)
        print(baud_rates)
        for port, packet in product(port_handlers, packet_handlers):
            self.port_handler = port_handlers[port]['handler']
            self.packet_handler = packet_handlers[packet]

            original_baud = port_handler[port]['baud rate']
            print("++++++++++++++++++++")
            print(original_baud)
            for baud in baud_rates:
                if original_baud is None:
                    self.port_handler.setBaudRate(baud)
                else:
                    continue
                pose, success = self.get_present_position()
                if success:
                    print("============", port, packet, baud)
                    self.port_name = port
                    self.protocol = packet
                    self.baud = baud
                    port_handler[port]['baud rate'] = baud
                    break
            if success:
                break
        self.verbosity = original_verbosity

        if not success:
            print("Helper: [ERROR] ID:{}, Alias:{}, Model:{}".format(
                self.id, self.alias, self.model))
            print("        Motor connection failed.")
            print("        Please check the connection or \"<preset>.json\".")
            print("        Common causes of this phenomenon like below:")
            print("          1. The motor is turned OFF.")
            print("          2. Some port descriptions are incorrect in JSON.")
            raise RuntimeError
        print("")

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
