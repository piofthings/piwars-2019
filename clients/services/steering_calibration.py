#!/usr/bin/env python3

import math
import time

from adafruit_servokit import ServoKit


class SteeringCalibration:

    __looper = True

    def __init__(self, arg):
        self.arg = arg
        self.main()

    def main(self):
        print("J2 Controller Main loop")
        print("Press <Esc> or Ctrl-C to exit")
        print()
        print("C: Wheel Calibration")
        print("")
        while self.__looper:
            keyp = readkey()

    #======================================================================
    # Reading single character by forcing stdin to raw mode
    import sys
    import tty
    import termios

    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch == '0x03':
            raise KeyboardInterrupt
        return ch

    def readkey(getchar_fn=None):
        getchar = getchar_fn or readchar
        c1 = getchar()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5b:
            return c1
        c3 = getchar()
        # 16=Up, 17=Down, 18=Right, 19=Left arrows
        return chr(0x10 + ord(c3) - 65)

    # End of single character reading
    #======================================================================
