#!/usr/bin/env python

from neck_mode.msg import dxl_target
from neck_mode.msg import dxl_feedback

import dynamixel_functions as dxl

import json


def read_json(filename):
    fd = open(filename)
    json_data = fd.read()
    fd.close()
    return json.loads(json_data)


class motor_set:
    print("motor_oper")

    def __init__(self, port_num, motor_config, addr_config_file):
        self.port_num = port_num
        self.config = motor_config
        self.addr = read_json(addr_config_file)
        self.target_pos = 0
        self.current_pos = 0
        self.currnet_pgain = 0
        self.current_igain = 0

    def torque_enable(self, enable):
        dxl.write1ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["TORQUE_ENABLE"], enable)

    def read_position_pgain(self):
        self.current_pgain = dxl.read2ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["POSITION_P_GAIN"])
        return self.current_pgain

    def read_position_igain(self):
        self.current_igain = dxl.read2ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["POSITION_I_GAIN"])
        return self.current_igain

    def set_position_pgain(self, pgain):
        dxl.write2ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["POSITION_P_GAIN"], pgain)

    def set_position_igain(self, igain):
        dxl.write2ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["POSITION_I_GAIN"], igain)

    def set_goal_pos(self, goal):
        dxl.write4ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["GOAL_POSITION"], goal)

    def read_cur_pos(self):
        self.current_pos = dxl.read4ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["PRESENT_POSITION"])
        return self.current_pos

    def spin(self):
        self.current_pos = dxl.readwrtie4ByteTxRx(
            self.port_num, self.config["protocol"], self.config["id"], self.addr["PRESENT_POSITION"])


class motor_operation:
    def __init__(self, pkg_dir):

        data = read_json(pkg_dir+"/config/dxl_config_xm.json")
        port_nums = []
        # open all ports in config file
        for port in data["port"]:
            port_nums.append(dxl.portHandler(port["device"].encode("utf-8")))

        for idx, port_num in enumerate(port_nums):
            if dxl.openPort(port_num):
                print("Succeed to open the port {}".format(idx))
            else:
                print("Failed to open the port {}".format(idx))
                quit()

        dxl.packetHandler()

        for i, port in enumerate(data["port"]):
            if dxl.setBaudRate(port_nums[i], data["port"][i]["baud"]):
                print("Succeeded to change the baudrate! port {} ".format(i))
                # print(data["port"][i])

            else:
                print("Failed to change the baudrate! port {}".format(i))
                quit()

        # reading motor info from config==========================================

        self.motors = []
        for idx, motor in enumerate(data["motor"]):
            port_num = port_nums[motor["port"]]
            addr_config_file = pkg_dir + \
                "/config/motor_type/"+motor["type"]+".json"
            motors = motor_set(port_num, motor, addr_config_file)
            self.motors.append(motors)

    def set_goal_pos(self, goals):
        for i, motor in enumerate(self.motors):
            motor.set_goal_pos(goals[i])

    def set_position_pgains(self, pgains):
        for i, motor in enumerate(self.motors):
            motor.set_position_pgain(pgains[i])

    def set_position_igains(self, igains):
        for i, motor in enumerate(self.motors):
            motor.set_position_igain(igains[i])

    def torque_enable(self, enables):
        for i, motor in enumerate(self.motors):
            motor.torque_enable(enables[i])

    def read_position_pgains(self):
        self.cur_pgains = []
        for i, motor in enumerate(self.motors):
            self.cur_pgains.append(motor.read_position_pgain())
        print(self.cur_pgains)
        return self.cur_pgains

    def read_position_igains(self):
        self.cur_igains = []
        for i, motor in enumerate(self.motors):
            self.cur_igains.append(motor.read_position_igain())
        print(self.cur_igains)
        return self.cur_igains

    def read_cur_pos(self):
        cur_poses = []
        for i, motor in enumerate(self.motors):
            cur_poses.append(motor.read_cur_pos())
        # print cur_poses
        return cur_poses

    def spin_all(self):
        for motor in self.motors:
            motor.spin()

    def dxl_target_callback(self):
        cur_pos = self.read_cur_pos()
        msg = dxl_feedback()
        msg.pos = [0, 0]

        msg.pos[0] = cur_pos[0]
        msg.pos[1] = cur_pos[1]
        print(msg.pos)


if __name__ == "__main__":
    mo = motor_operation(sys.argv[1])
    mo.torque_enable([1, 1])
    mo.set_goal_pos([100, 2048])
