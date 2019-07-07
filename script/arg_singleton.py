#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Argument based Singleton
# https://stackoverflow.com/questions/39033946/python-argument-based-singleton

# class Singleton(type):
#     __instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.__instances:
#             cls.__instances[cls] = super().__call__(*args, **kwargs)
#         return cls.__instances[cls]
