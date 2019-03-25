#!/usr/bin/env python3

import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

from keyboard_input import KeyboardInput
from gpiozero import DigitalOutputDevice

RELAY_1 = 17  # Green
RELAY_2 = 27  # Yellow
RELAY_3 = 22  # Orange
RELAY_4 = 23  # Red
RELAY_5 = 24  # Brown

relay1 = DigitalOutputDevice(pin=RELAY_1)
relay2 = DigitalOutputDevice(pin=RELAY_2)
relay3 = DigitalOutputDevice(pin=RELAY_3)
relay4 = DigitalOutputDevice(pin=RELAY_4)
relay5 = DigitalOutputDevice(pin=RELAY_5)
keyboardInput = KeyboardInput("Trigger Prototype")
keyPress = ''

while keyPress != 'q':
    keyboardInput.clear()
    print("Meteor Shooter")
    print("Press <Esc> or Ctrl-C to exit")
    print("1: Aim 1")
    print("2: Aim 2")
    print("3: Aim 3")
    print("4: Aim 4")
    print("5: Aim 5")
    print("--------------------")
    print("q: Quit")
    print("")
    keyPress = keyboardInput.readkey()
    if keyPress == '1':
        if(relay1.value == 1):
            relay1.off()
        else:
            relay1.on()
    if keyPress == '2':
        if(relay2.value == 1):
            relay2.off()
        else:
            relay2.on()
    if keyPress == '3':
        if(relay3.value == 1):
            relay3.off()
        else:
            relay3.on()
    if keyPress == '4':
        if(relay4.value == 1):
            relay4.off()
        else:
            relay4.on()
    if keyPress == '5':
        if(relay5.value == 1):
            relay5.off()
        else:
            relay5.on()
