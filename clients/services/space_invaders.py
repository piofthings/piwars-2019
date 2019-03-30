
#!/usr/bin/env python3

import time
import sys
import os

from gpiozero import DigitalOutputDevice
from adafruit_servokit import ServoKit


class SpaceInvaders():
    """docstring for SpaceInvaders."""
    __kit = None

    TRIGGER_1 = 7
    TRIGGER_2_3 = 8
    TRIGGER_4_5 = 3

    REST = 60
    FIRE_EVEN = 120
    FIRE_ODD = 0

    TRIGGER_WAIT = 1 / 5

    RELAY_1 = 17  # Green
    RELAY_2 = 27  # Yellow
    RELAY_3 = 22  # Orange
    RELAY_4 = 23  # Red
    RELAY_5 = 24  # Brown

    def __init__(self, kit):
        self.__kit = kit
        self.__kit.servo[self.TRIGGER_1].angle = self.REST
        self.__kit.servo[self.TRIGGER_2_3].angle = self.REST
        self.__kit.servo[self.TRIGGER_4_5].angle = self.REST
        self.__relay1 = DigitalOutputDevice(pin=self.RELAY_1)
        self.__relay2 = DigitalOutputDevice(pin=self.RELAY_2)
        self.__relay3 = DigitalOutputDevice(pin=self.RELAY_3)
        self.__relay4 = DigitalOutputDevice(pin=self.RELAY_4)
        self.__relay5 = DigitalOutputDevice(pin=self.RELAY_5)

    def aim(self, index):
        if index == 1:
            self.__relay1.on()
        if index == 2:
            self.__relay2.on()
        if index == 3:
            self.__relay3.on()
        if index == 4:
            self.__relay4.on()
        if index == 5:
            self.__relay5.on()

    def launch(self, index):
        if index == 1:
            self.__kit.servo[self.TRIGGER_1].angle = self.FIRE_EVEN
            time.sleep(self.TRIGGER_WAIT)
            self.__kit.servo[self.TRIGGER_1].angle = self.REST
            self.__relay1.off()
        if index == 2:
            self.__kit.servo[self.TRIGGER_2_3].angle = self.FIRE_EVEN
            time.sleep(self.TRIGGER_WAIT)
            self.__kit.servo[self.TRIGGER_2_3].angle = self.REST
            self.__relay2.off()
        if index == 3:
            self.__kit.servo[self.TRIGGER_2_3].angle = self.FIRE_ODD
            time.sleep(self.TRIGGER_WAIT)
            self.__kit.servo[self.TRIGGER_2_3].angle = self.REST
            self.__relay3.off()
        if index == 4:
            self.__kit.servo[self.TRIGGER_4_5].angle = self.FIRE_EVEN
            time.sleep(self.TRIGGER_WAIT)
            self.__kit.servo[self.TRIGGER_4_5].angle = self.REST
            self.__relay4.off()
        if index == 5:
            self.__kit.servo[self.TRIGGER_4_5].angle = self.FIRE_ODD
            time.sleep(self.TRIGGER_WAIT)
            self.__kit.servo[self.TRIGGER_4_5].angle = self.REST
            self.__relay5.off()
