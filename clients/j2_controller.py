#!/usr/bin/env python3
import math
import time
import sys
import os
from bluedot.btcomm import BluetoothClient

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
    __bt_client = BluetoothClient("j2cruncher", data_received)

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
            # elif (keyp == 'd' or keyp == 'd'):

            time.sleep(0.01)

    def __menu(self):
        self.__keyboardInput.clear()
        print("J2 Controller")
        print("Press <Esc> or Ctrl-C to exit")
        print("c: Wheel Calibration")
        print("d: Test drive")
        print("--------------------")
        print("q: Quit")
        print("")

    def data_received(data):
        print(data)


j2 = J2controller(sys.argv)
j2.init()

# bt_client.py
# from bluedot.btcomm import BluetoothClient
# from signal import pause
#
# def data_received(data):
#     print(data)
#
# c.send("helloworld")
#
# pause()
