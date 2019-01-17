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
        print()
        print("c: Configure wheel indexes (On Adafruit PWM Board)")
        print("w: Front left Wheel")
        print("e: Front right Wheel")
        print("s: Rear left Wheel")
        print("d: Rear right Wheel")
        print("r: Save current status")
        print("0: Reset all to 90")
        print("--------------------")
        print("q: Back")
        print("")
        self.waitForInput()

    def waitForInput(self):
        while self.__looper:
            keyp = self.__keyboardInput.readkey()
            if(keyp == 'q'):
                self.save_steering_status()
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
            elif(keyp == 'w'):
                self.calibrate_steering(1)
            elif(keyp == 'e'):
                self.calibrate_steering(2)
            elif(keyp == 's'):
                self.calibrate_steering(3)
            elif(keyp == 'd'):
                self.calibrate_steering(4)
            elif(keyp == 'r'):
                self.save_steering_status()
                print("Saved to file", end='\r', flush=True)
            elif(keyp == '0'):
                self.__steering_status.front_left_delta = 90
                self.__steering_status.front_right_delta = 90
                self.__steering_status.rear_left_delta = 90
                self.__steering_status.rear_right_delta = 90
                self.__update_servos()
            time.sleep(0.01)

    def calibrate_steering(self, index):
        waitForWheel = True
        keyboardInput = KeyboardInput("Calibrate Steering:")
        print("Press Up/Down or w/z to adjust wheel delta, 0 to reset, q when done")
        while waitForWheel:
            key = keyboardInput.readkey()
            if(key == 'w' or ord(key) == 16):
                if(index == 1):
                    self.__steering_status.front_left_delta = self.__steering_status.front_left_delta + 1
                    print("\r front_left_delta: " +
                          str(self.__steering_status.front_left_delta), end='\r', flush=True)
                elif(index == 2):
                    self.__steering_status.front_right_delta = self.__steering_status.front_right_delta + 1
                    print("\r front_right_delta: " +
                          str(self.__steering_status.front_right_delta), end='\r', flush=True)
                elif(index == 3):
                    self.__steering_status.rear_left_delta = self.__steering_status.rear_left_delta + 1
                    print("\r rear_left_delta: " +
                          str(self.__steering_status.rear_left_delta), end='\r', flush=True)
                elif(index == 4):
                    self.__steering_status.rear_right_delta = self.__steering_status.rear_right_delta + 1
                    print("\r rear_right_delta: " +
                          str(self.__steering_status.rear_right_delta), end='\r', flush=True)

                self.__update_servos()
            elif(key == 'z' or ord(key) == 17):
                if(index == 1):
                    if(self.__steering_status.front_left_delta > 0):
                        self.__steering_status.front_left_delta = self.__steering_status.front_left_delta - 1
                        print("\r front_left_delta: " +
                              str(self.__steering_status.front_left_delta), end='\r', flush=True)
                elif(index == 2):
                    if(self.__steering_status.front_right_delta > 0):
                        self.__steering_status.front_right_delta = self.__steering_status.front_right_delta - 1
                        print("\r front_right_delta: " +
                              str(self.__steering_status.front_right_delta), end='\r', flush=True)
                elif(index == 3):
                    if(self.__steering_status.rear_left_delta > 0):
                        self.__steering_status.rear_left_delta = self.__steering_status.rear_left_delta - 1
                    print("\r rear_left_delta: " +
                          str(self.__steering_status.rear_left_delta), end='\r', flush=True)
                elif(index == 4):
                    if(self.__steering_status.rear_right_delta > 0):
                        self.__steering_status.rear_right_delta = self.__steering_status.rear_right_delta - 1
                        print("\r rear_right_delta: " +
                              str(self.__steering_status.rear_right_delta), end='\r', flush=True)
                self.__update_servos()

            elif(key == 'q'):
                self.save_steering_status()
                waitForWheel = False
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
        self.__steering_status.front_left_delta = self.__kit.servo[int(
            self.__steering_status.front_left_port)].angle
        self.__steering_status.front_right_delta = self.__kit.servo[int(
            self.__steering_status.front_right_port)].angle
        self.__steering_status.rear_left_delta = self.__kit.servo[int(
            self.__steering_status.rear_left_port)].angle
        self.__steering_status.rear_right_delta = self.__kit.servo[int(
            self.__steering_status.rear_right_port)].angle
        self.__steering_status.save()

    def __update_servos(self):
        self.__kit.servo[int(self.__steering_status.front_left_port)
                         ].angle = self.__steering_status.front_left_delta
        self.__kit.servo[int(self.__steering_status.front_right_port)
                         ].angle = self.__steering_status.front_right_delta
        self.__kit.servo[int(self.__steering_status.rear_left_port)
                         ].angle = self.__steering_status.rear_left_delta
        self.__kit.servo[int(self.__steering_status.rear_right_port)
                         ].angle = self.__steering_status.rear_right_delta
