#!/usr/bin/env python3

import time
import sys, os

from adafruit_servokit import ServoKit
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

from keyboard_input import KeyboardInput

kit = ServoKit(channels=16)

TRIGGER_1 = 7
TRIGGER_2_3 = 8
TRIGGER_4_5 = 9

REST = 60
FIRE_EVEN = 120
FIRE_ODD = 0

TRIGGER_WAIT = 1/5
kit.servo[TRIGGER_1].angle = REST
kit.servo[TRIGGER_2_3].angle = REST
kit.servo[TRIGGER_4_5].angle = REST
keyboardInput = KeyboardInput("J2Controller")
keyPress = ''

while keyPress != 'q':
    keyboardInput.clear()
    print("Meteor Shooter")
    print("Press <Esc> or Ctrl-C to exit")
    print("1: Fire 1")
    print("2: Fire 2")
    print("3: Fire 3")
    print("4: Fire 4")
    print("5: Fire 5")
    print("--------------------")
    print("u: Up 3")
    print("n: Down 3")
    print("j: Zero 3")
    print("--------------------")
    print("q: Quit")
    print("")
    keyPress = keyboardInput.readkey()
    if keyPress == '1':
        kit.servo[TRIGGER_1].angle = FIRE_EVEN
        time.sleep(TRIGGER_WAIT)
        kit.servo[TRIGGER_1].angle = REST
    if keyPress == '2':
        kit.servo[TRIGGER_2_3].angle = FIRE_EVEN
        time.sleep(TRIGGER_WAIT)
        kit.servo[TRIGGER_2_3].angle = REST
    if keyPress == '3':
        kit.servo[TRIGGER_2_3].angle = FIRE_ODD
        time.sleep(TRIGGER_WAIT)
        kit.servo[TRIGGER_2_3].angle = REST
    if keyPress == '4':
        kit.servo[TRIGGER_4_5].angle = FIRE_EVEN
        time.sleep(TRIGGER_WAIT)
        kit.servo[TRIGGER_4_5].angle = REST
    if keyPress == '5':
        kit.servo[TRIGGER_4_5].angle = FIRE_ODD
        time.sleep(TRIGGER_WAIT)
        kit.servo[TRIGGER_4_5].angle = REST
    elif keyPress == 'u':
        kit.servo[TRIGGER_4_5].angle = kit.servo[TRIGGER_4_5].angle + 5
    elif keyPress == 'n':
        kit.servo[TRIGGER_4_5].angle = kit.servo[TRIGGER_4_5].angle - 5
    elif keyPress == 'j':
        kit.servo[TRIGGER_4_5].angle = 0
#time.sleep(2)
#kit.servo[TRIGGER_0].angle = max
#kit.servo[5].angle = max
