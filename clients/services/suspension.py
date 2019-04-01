#!/usr/bin/env python3

import time
from adafruit_servokit import ServoKit
from keyboard_input import KeyboardInput


class Suspension:
    __looper = True
    __keyboardInput = KeyboardInput
    __kit = None
    MIN_ANGLE = 115
    MAX_ANGLE = 0

    def __init__(self, servoKit):
        if (servoKit != None):
            self.__kit = servoKit
            self.__kit.servo[4].angle = self.MIN_ANGLE
            self.__kit.servo[5].angle = self.MIN_ANGLE

    def raise_front_by(self, degrees):
        final = self.__kit.servo[4].angle - degrees
        if(final > self.MAX_ANGLE):
            self.__kit.servo[4].angle = final
        else:
            self.__kit.servo[4].angle = self.MAX_ANGLE

    def raise_rear_by(self, degrees):
        final = self.__kit.servo[4].angle - degrees
        if(final > self.MAX_ANGLE):
            self.__kit.servo[5].angle = final
        else:
            self.__kit.servo[5].angle = self.MAX_ANGLE

    def lower_front_by(self, degrees):
        final = self.__kit.servo[4] + degrees
        if(final < self.MIN_ANGLE):
            self.__kit.servo[4].angle = final
        else:
            self.__kit.servo[4].angle = self.MIN_ANGLE

    def raise_both_by(self, degrees):
        final = self.__kit.servo[4].angle - degrees
        if(final > self.MAX_ANGLE):
            self.__kit.servo[4].angle = final
            self.__kit.servo[5].angle = final
        else:
            self.__kit.servo[4].angle = self.MAX_ANGLE
            self.__kit.servo[5].angle = self.MAX_ANGLE

    def lower_both_by(self, degrees):
        final = self.__kit.servo[4] + degrees
        if(final < self.MIN_ANGLE):
            self.__kit.servo[4].angle = final
            self.__kit.servo[5].angle = final
        else:
            self.__kit.servo[4].angle = self.MIN_ANGLE
            self.__kit.servo[5].angle = self.MIN_ANGLE
