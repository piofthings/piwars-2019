#!/usr/bin/env python3
import math
import time
import sys
import os

from adafruit_servokit import ServoKit


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))
from dc_drive import DcDrive
from steering import Steering
from suspension import Suspension
from steering_calibration import SteeringCalibration
from keyboard_input import KeyboardInput


class J2controller():
    """The J2 Controller Main processing loop"""
    __looper = True
    __kit = ServoKit(channels=16)
    __keyboardInput = KeyboardInput("J2Controller")

    def __init__(self, arg):
        self.arg = arg
        # self.main()

    def init(self):
        self.__menu()
        while self.__looper:
            keyp = self.__keyboardInput.readkey()
            print(keyp)
            if (keyp == 'q'):
                self.__looper = False
            elif (keyp == 'c' or keyp == 'C'):
                sc = SteeringCalibration(self.__kit)
                sc.menu()
                self.__menu()

            time.sleep(0.01)

    def __menu(self):
        self.__keyboardInput.clear()
        print("J2 Controller")
        print("Press <Esc> or Ctrl-C to exit")
        print("c: Wheel Calibration")
        print("--------------------")
        print("q: Quit")
        print("")


j2 = J2controller(sys.argv)
j2.init()
