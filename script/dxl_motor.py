#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ModifiedSingleton(type):
    __instances = {}

    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls.__instances:
    #         cls.__instances[cls] = super().__call__(*args, **kwargs)
    #     return cls.__instances[cls]


class DxlMotor(metaclass=ModifiedSingleton):
    def __init__(self, id, alias, port_handle, packet_handle):



# class Test(metaclass=Singleton):
#     def __init__(self, a):
#         self.a = a


# if __name__=="__main__":
#     k = Test(3)
#     print(k.a)
#     t1 = Test(3)
#     t2 = Test(4)
#     print(t1.a)
#     print(t2.a)
