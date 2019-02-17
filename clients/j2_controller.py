#!/usr/bin/env python3
import math
import time
import sys
import os
import atexit

from bluedot.btcomm import BluetoothClient

from adafruit_servokit import ServoKit


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "models")))

from gpiozero_drive import GpiozeroDrive
from steering import Steering
from suspension import Suspension
from steering import Steering
from servo_calibration import ServoCalibration

from bt_request import BtRequest
from piconzero_drive import PiconzeroDrive

from terminal_menu import TerminalMenu


class J2controller():
    """The J2 Controller Main processing loop"""
    __looper = True
    __kit = None
    __bt_client = None
    __terminalMenu = TerminalMenu()
    __piconzero_drive = PiconzeroDrive()

    def __init__(self, arg):
        self.arg = arg
        atexit.register(self.cleanup)

        try:
            self.__kit = ServoKit(channels=16)
        except:
            print("Servokit not initialised, Servo Calibration won't work")
        try:
            self.__bt_client = BluetoothClient("tinycruncher", self.data_received)
            print("Bluetooth client initialised, ready for Cruncher comms:")

        except:
            print("Bluetooth client not initialised, Cruncher comms won't work")

        # self.main()

    def init(self):
        #
        while self.__looper:
            #keyp = self.__terminalMenu.keyPress
            # if (keyp == 'q'):
            #    self.__looper = False
            # elif (keyp == 'c' or keyp == 'C'):
            #    sc = ServoCalibration(self.__kit)
            #    sc.menu()
                # self.__menu()
            # elif (keyp == 'd' or keyp == 'd'):

            time.sleep(1 / 60)

    def data_received(self, data_string):
        #print("BT Recieved:" + data_string)
        try:
            request = BtRequest(json_def=data_string)
            if(request.cmd == "steering" and request.action == "move"):
                self.__piconzero_drive.move(int(request.data.directionLeft), int(request.data.directionRight), float(request.data.speedLeft), float(request.data.speedRight))
        except:
            type, value, traceback = sys.exc_info()
            print('Error Deserialising %s: %s %s' % (data_string, type, value))

    def cleanup(self):
        if(self.__piconzero_drive != None):
            self.__piconzero_drive.cleanup()


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
