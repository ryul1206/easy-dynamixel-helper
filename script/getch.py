#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# This function get one 'char' without pressing 'enter'
# And also return one char you pressed.
if os.name == 'nt':
    import msvcrt

    def getch():
        return msvcrt.getch().decode()
else:
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def getch_exit(msg=''):
    print(msg)
    print("Press any key to exit ...")
    getch()
    exit()


def getch_ask(msg=''):
    if msg:
        print(msg)
    print("Press any key to continue ... (Press ESC to exit)")
    if getch() == chr(0x1b):
        exit()


if __name__ == "__main__":
    print("Press any key to continue ...")
    print(getch())
