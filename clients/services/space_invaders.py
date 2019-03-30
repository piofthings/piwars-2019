
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

    __relay1 = DigitalOutputDevice(pin=RELAY_1)
    __relay2 = DigitalOutputDevice(pin=RELAY_2)
    __relay3 = DigitalOutputDevice(pin=RELAY_3)
    __relay4 = DigitalOutputDevice(pin=RELAY_4)
    __relay5 = DigitalOutputDevice(pin=RELAY_5)

    __kit.servo[TRIGGER_1].angle = REST
    __kit.servo[TRIGGER_2_3].angle = REST
    __kit.servo[TRIGGER_4_5].angle = REST

    def __init__(self, kit):
        self.__kit = kit

    def aim(self, index):
        if index == 1:
            relay1.on()
        if index == 2:
            relay2.on()
        if index == 3:
            relay3.on()
        if index == 4:
            relay4.on()
        if index == 5:
            relay5.on()

    def launch(self, index):
        if index == 1:
            self._kit.servo[TRIGGER_1].angle = FIRE_EVEN
            time.sleep(TRIGGER_WAIT)
            self._kit.servo[TRIGGER_1].angle = REST
        if index == 2:
            self._kit.servo[TRIGGER_2_3].angle = FIRE_EVEN
            time.sleep(TRIGGER_WAIT)
            self._kit.servo[TRIGGER_2_3].angle = REST
        if index == 3:
            self._kit.servo[TRIGGER_2_3].angle = FIRE_ODD
            time.sleep(TRIGGER_WAIT)
            self._kit.servo[TRIGGER_2_3].angle = REST
        if index == 4:
            self._kit.servo[TRIGGER_4_5].angle = FIRE_EVEN
            time.sleep(TRIGGER_WAIT)
            self._kit.servo[TRIGGER_4_5].angle = REST
        if index == 5:
            self._kit.servo[TRIGGER_4_5].angle = FIRE_ODD
            time.sleep(TRIGGER_WAIT)
            self._kit.servo[TRIGGER_4_5].angle = REST
