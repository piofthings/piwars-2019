#!/usr/bin/env python3

import math
import time
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")
from steering_status import SteeringStatus
from keyboard_input import KeyboardInput


class SteeringCalibration:
    __kit = None
    __looper = True
    __keyboardInput = None

    def __init__(self, servoKit):
        self.__kit = servoKit
        self.__keyboardInput = KeyboardInput("Steering Calibration")
        self.__steering_status = SteeringStatus(
            json_file=os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..")) + "/config/steering_status.json")

    def menu(self):
        self.__keyboardInput.clear()
        print("J2 Controller Steering Calibration loop")
        print("Press <Esc> or Ctrl-C to exit")
        print()
        print("c: Configure wheel indexes (On Adafruit PWM Board)")
        print("w: Front left Wheel")
        print("e: Front right Wheel")
        print("s: Rear left Wheel")
        print("d: Rear right Wheel")
        print("--------------------")
        print("q: Back")
        print("")
        self.waitForInput()

    def waitForInput(self):
        while self.__looper:
            keyp = self.__keyboardInput.readkey()
            if(keyp == 'q'):
                self.__looper = False
            elif(keyp == 'c'):
                print("Enter Port on which front_left steering motor is: ")
                self.set_steering_status(1, input())
                print("Enter Port on which front_right steering motor is: ")
                self.set_steering_status(2, input())
                print("Enter Port on which rear_left steering motor is: ")
                self.set_steering_status(3, input())
                print("Enter Port on which rear_right steering motor is: ")
                self.set_steering_status(4, input())
                self.save_steering_status()
            time.sleep(0.01)

    def set_steering_status(self, index, value):
        if(index == 1):
            self.__steering_status.front_left_port = value
        elif(index == 2):
            self.__steering_status.front_right_port = value
        elif(index == 3):
            self.__steering_status.rear_left_port = value
        elif(index == 4):
            self.__steering_status.rear_right_port = value

    def save_steering_status(self):
        self.__steering_status.save()
