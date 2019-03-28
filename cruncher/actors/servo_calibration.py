#!/usr/bin/env python3
"""

"""
import math
import time
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")
from steering_status import SteeringStatus
from keyboard_input import KeyboardInput
from steering import Steering


class ServoCalibration:
    __kit = None
    __looper = True
    __keyboardInput = None
    __steering = None

    def __init__(self, servoKit):
        self.__kit = servoKit
        self.__keyboardInput = KeyboardInput("Steering Calibration")
        self.__steering = Steering(self.__kit, steeringStatusFile=os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..")) + "/config/steering_status.json")

    def increment_position(self, index, value):
        if(key == 'w'):
            self.__steering.increment_position(index, 1)
            self.__steering.update_servos()
        elif(ord(key) == 16):
            self.__steering.move_servo_by(index, 1)
        elif(key == 'z'):
            self.__steering.decrement_position(index, 1)
            self.__steering.update_servos()
        elif(ord(key) == 17):
            self.__steering.move_servo_by(index, -1)
        elif(key == 'q'):
            self.__steering.save_steering_status()
            waitForWheel = False
        time.sleep(0.01)
