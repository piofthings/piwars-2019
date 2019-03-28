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
from gpiozero_drive import GpiozeroDrive

from terminal_menu import TerminalMenu


class J2controller():
    """The J2 Controller Main processing loop"""
    __looper = True
    __kit = None
    __bt_client = None
    __terminalMenu = TerminalMenu()
    __piconzero_drive = None  # PiconzeroDrive()
    __gpiozero_drive = GpiozeroDrive()
    __steering = None
    __debug = False

    def __init__(self, arg):
        self.args = arg
        isDebug = False
        if(len(self.args) > 1):
            print("\n".join(self.args[1:]))
            if(self.args[1] == "debug"):
                self.__debug = True
        atexit.register(self.cleanup)

        self.__connect_to_cruncher()
        try:
            self.__kit = ServoKit(channels=16)
        except:
            print("Servokit not initialised, Servo Calibration won't work")

        try:
            self.__steering = Steering(self.__kit, steeringStatusFile=os.path.abspath("./config/steering_status.json"))
        except:
            type, value, traceback = sys.exc_info()
            print("Steering status failed to load")
            print('Error Details %s: %s %s' % (type, value, traceback))

    def init(self):
        while self.__looper:
            if(self.__bt_client == None):
                self.__connect_to_cruncher()
            elif (self.__bt_client.connected == False):
                try:
                    print("Trying to connect")
                    self.__bt_client.connect()
                except KeyboardInterrupt:
                    self.__looper = False
                    self.cleanup()
                except:
                    type, value, traceback = sys.exc_info()
                    print('Error Details %s: %s %s' % (type, value, traceback))
            time.sleep(1 / 60)

    def __connect_to_cruncher(self):
        try:
            self.__bt_client = BluetoothClient("B8:27:EB:55:22:18", self.data_received, auto_connect=True)
            if(self.__debug):
                print("Bluetooth client initialised, ready for Cruncher comms:")

        except:
            type, value, traceback = sys.exc_info()
            if(self.__debug):
                print("Bluetooth client not initialised, Cruncher comms won't work")
                print('Error Details %s: %s %s' % (type, value, traceback))
            time.sleep(1)

    def data_received(self, data_string):
        print("BT Recieved:" + data_string)
        try:
            lines = data_string.splitlines()
            request = BtRequest(json_def=lines[0])
            if(request.cmd == "calibrate"):
                if(request.action == "getStatus"):
                    self.bt_request.send(json.dumps(self.__steering.steering()))
                elif(request.action == "setStatus"):
                    # self.bt_request.s
                    pass
            if(request.cmd == "steering"):
                if(request.action == "move"):
                    self.__gpiozero_drive.move(int(request.data.directionLeft), int(request.data.directionRight), float(request.data.speedLeft), float(request.data.speedRight))
            if(request.cmd == "wheels"):
                if(request.action == "strafe"):
                    if(self.__debug):
                        print("Strafing")
                    self.__steering.move_servo_to(Steering.FRONT_LEFT_POS, int(request.data.frontLeftAngle))
                    self.__steering.move_servo_to(Steering.FRONT_RIGHT_POS, int(request.data.frontRightAngle))
                    self.__steering.move_servo_to(Steering.REAR_LEFT_POS, int(request.data.rearLeftAngle))
                    self.__steering.move_servo_to(Steering.REAR_RIGHT_POS, int(request.data.rearRightAngle))
            if(request.cmd == "shooter"):
                if(request.action == "aim"):
                    # Turn laser on
                    pass
                elif(request.action == "launch"):
                    # Fire appropriate cannon
                    pass

        except:
            type, value, traceback = sys.exc_info()
            if(self.__debug):
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
