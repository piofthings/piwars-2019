#!/usr/bin/env python3
import math
import time
import sys
import os
import atexit

from bluedot.btcomm import BluetoothClient

from adafruit_servokit import ServoKit


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../models")))

#from gpiozero_drive import GpiozeroDrive
from steering import Steering
from suspension import Suspension
from servo_calibration import ServoCalibration

#from bt_request import BtRequest
#from piconzero_drive import PiconzeroDrive
#from gpiozero_drive import GpiozeroDrive

from terminal_menu import TerminalMenu


class TerminalController():
    """The J2 Controller Main processing loop"""
    __looper = True
    __kit = None
    __bt_client = None
    __terminalMenu = TerminalMenu()
    __piconzero_drive = None  # PiconzeroDrive()
    __gpiozero_drive = None  # GpiozeroDrive()
    __steering = None

    def __init__(self, arg):
        self.arg = arg
        atexit.register(self.cleanup)

        try:
            self.__kit = ServoKit(channels=16)
        except:
            print("Servokit not initialised, Servo Calibration won't work")

        try:
            self.__steering = Steering(self.__kit, steeringStatusFile=os.path.abspath("../config/steering_status.json"))
        except:
            type, value, traceback = sys.exc_info()
            print("Steering status failed to load")
            print('Error Details %s: %s %s' % (data_string, type, value))

    def init(self):
        while self.__looper:
            keyp = self.__terminalMenu.menu()

            if (keyp == 'q'):
                self.__looper = False
            elif (keyp == 'c' or keyp == 'C'):
                sc = ServoCalibration(self.__kit)
                sc.menu()
                # self.__menu()
            elif (keyp == 'd' or keyp == 'd'):
                pass
            time.sleep(1 / 60)

    def cleanup(self):
        if(self.__piconzero_drive != None):
            self.__piconzero_drive.cleanup()


j2 = TerminalController(sys.argv)
j2.init()
