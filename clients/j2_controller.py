#!/usr/bin/env python3
import math
import time
import sys
import os
from bluedot.btcomm import BluetoothClient

from adafruit_servokit import ServoKit


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "models")))

from dc_drive import GpiozeroDrive
from steering import Steering
from suspension import Suspension
from steering import Steering
from steering_calibration import ServoCalibration

from bt_request import BtRequest
from piconzero_drive import PiconzeroDrive

from terminal_menu import TerminalMenu


class J2controller():
    """The J2 Controller Main processing loop"""
    __looper = True
    __kit = ServoKit(channels=16)
    __bt_client = BluetoothClient("j2cruncher", self.data_received)
    __terminalMenu = TerminalMenu()
    __piconzero_drive = PiconzeroDrive()

    def __init__(self, arg):
        self.arg = arg
        # self.main()

    def init(self):
        self.__menu()
        while self.__looper:
            keyp = self.__terminalMenu.keyPress
            print(keyp)
            if (keyp == 'q'):
                self.__looper = False
            elif (keyp == 'c' or keyp == 'C'):
                sc = ServoCalibration(self.__kit)
                sc.menu()
                # self.__menu()
            # elif (keyp == 'd' or keyp == 'd'):

            time.sleep(1 / 60)

    def data_received(self, data_string):
        print(data_string)
        request = BtRequest(json_def=data_string)
        if(request.cmd == "steering" and request.action == "move"):
            self.__piconzero_drive.move(float(request.data.directionLeft), float(request.data.directionRight), float(request.data.speedLeft), float(request.data.speedRight))


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
