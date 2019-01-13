#!/usr/bin/env python3

import math
import time

import sqlite3

from adafruit_servokit import ServoKit


class Steering():
    FRONT_LEFT_POS = 11
    FRONT_RIGHT_POS = 10
    REAR_LEFT_POS = 0
    REAR_RIGHT_POS = 1

    __kit = None
    __Do = 0

    __init__(self, servoKit):
        self.__kit = servoKit
        self.__frontLeftServo = __kit.servo[11]
        self.__rearLeftServo = __kit.servo[10]
        self.__frontRightServo = __kit.servo[0]
        self.__rearRightServo = __kit.servo[1]

    #======================================================================
    # Reading single character by forcing stdin to raw mode
    import sys
    import tty
    import termios

    def readchar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch == '0x03':
            raise KeyboardInterrupt
        return ch

    def readkey(self, getchar_fn=None):
        getchar = getchar_fn or readchar
        c1 = getchar()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5b:
            return c1
        c3 = getchar()
        # 16=Up, 17=Down, 18=Right, 19=Left arrows
        return chr(0x10 + ord(c3) - 65)

    # End of single character reading
    #======================================================================

    def init(self, servoKit):
        # ServoKit(channels=16)
        __kit = servoKit

        __frontLeftServo.angle = 0
        __rearLeftServo.angle = 0
        __frontRightServo.angle = 0
        __rearRightServo.angle = 0

    def spotTurn(self):
        flVal = 45
        frVal = 135
        blVal = 135
        brVal = 45
        __frontLeftServo.angle = blVal
        __rearLeftServo.angle = blVal
        __frontRightServo.angle = frVal
        __rearRightServo.angle = brVal

    """
    L = Distance between front wheel and rear wheel
        L = 178
    R = Distance between Turn Center and center of gravity of the car
    t = Distance between rear wheel pivots
        t = 90
    Outer wheel angle Do = L/(R + t/2)
    Inner wheel angle Di = L/(R - t/2)

    Given we want to turn the bot by say 5 degrees of turn in the outer wheel
    we want to calculate what the inner wheel turn angle is and vice-versa

    The angle of turn determines R, so for Do = 5 degrees = (0.08726646 Radians) we need to calculate R
    first:

    Do x (R + t/2) = L
    R + t/2 = L/Do
    R = L/Do - t/2
      = (178/0.08726646 - 90/2)
    For L = 178, t = 90, Do = 0.08726646, R = 1996

    Now we calculate Di as

    Di = 178 / 1996 - 90/2
       = 178 / 1996 - 45
       = 178 / 1951
       = 0.0912 Radians = 5.225375 degress

    As we can see Di is more than Do which is correct as per Ackerman Steering theory.

    """

    def calculateDi(self, degree):
        L = 178
        t = 90
        Do = math.radians(degree)
        Ro = L / Do - t / 2
        return math.degrees(Ro)

    def angleAbsoluteLeft(self, degrees):
        self.__Do = degrees
        self.__Di = self.calculateDi(degrees)

    def angleAbsoluteRight(self, degrees):
        self.__Do = degrees * -1
        self.__Di = self.calculate(degrees * -1)

    def waitForInput(self):
        speed = 60

        print("Tests the servos by using the arrow keys to control")
        print("Press <space> key to centre")
        print("Press Ctrl-C to end")

        # main loop
        try:
            while True:
                keyp = readkey()
                if keyp == 'c':
                    self.spotTurn()

        #        if keyp == 'w' or ord(keyp) == 16:
        #            panVal = max (0, panVal - 5)
        #            print 'Up', panVal
        #        elif keyp == 'z' or ord(keyp) == 17:
        #            panVal = min (180, panVal + 5)
        #            print 'Down', panVal
        #        elif keyp == 's' or ord(keyp) == 18:
        #            tiltVal = max (0, tiltVal - 5)
        #            print 'Right', tiltVal
        #        elif keyp == 'a' or ord(keyp) == 19:
        #            tiltVal = min (180, tiltVal + 5)
        #            print 'Left', tiltVal
        #        elif keyp == 'g':
        #            gripVal = max (0, gripVal - 5)
        #            print 'Open', gripVal
        #        elif keyp == 'h':
        #            gripVal = min (180, gripVal + 5)
        #            print 'Close', gripVal
                elif keyp == ' ':
                    flVal = frVal = blVal = brVal = 90
                    print('Centre')
                elif ord(keyp) == 3:
                    break
                pz.setOutput(front_left, flVal)
                pz.setOutput(front_right, frVal)
                pz.setOutput(back_left, blVal)
                pz.setOutput(back_right, brVal)

        except KeyboardInterrupt:
            print

        finally:
            pz.cleanup()


"""
# Picon Zero Servo Test
# Use arrow keys to move 2 servos on outputs 0 and 1 for Pan and Tilt
# Use G and H to open and close the Gripper arm
# Press Ctrl-C to stop
#

import piconzero as pz, time

#======================================================================
# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

# End of single character reading
#======================================================================

speed = 60

print("Tests the servos by using the arrow keys to control")
print("Press <space> key to centre")
print("Press Ctrl-C to end")
print

# Define which pins are the servos
front_left = 0
front_right = 3
back_left = 1
back_right = 2

pz.init()

# Set output mode to Servo
pz.setOutputConfig(front_left, 2)
pz.setOutputConfig(front_right, 2)
pz.setOutputConfig(back_left, 2)
pz.setOutputConfig(back_right, 2)

# Centre all servos
flVal = 90
frVal = 90
blVal = 90
brVal = 90

pz.setOutput (front_right, frVal)
pz.setOutput (back_left, blVal)
pz.setOutput (back_right, brVal)

# main loop
try:
 while True:
  keyp = readkey()
  if keyp == 'c':
   flVal = 45
   frVal = 135
   blVal = 130
   brVal = 45
#        if keyp == 'w' or ord(keyp) == 16:
#            panVal = max (0, panVal - 5)
#            print 'Up', panVal
#        elif keyp == 'z' or ord(keyp) == 17:
#            panVal = min (180, panVal + 5)
#            print 'Down', panVal
#        elif keyp == 's' or ord(keyp) == 18:
#            tiltVal = max (0, tiltVal - 5)
#            print 'Right', tiltVal
#        elif keyp == 'a' or ord(keyp) == 19:
#            tiltVal = min (180, tiltVal + 5)
#            print 'Left', tiltVal
#        elif keyp == 'g':
#            gripVal = max (0, gripVal - 5)
#            print 'Open', gripVal
#        elif keyp == 'h':
#            gripVal = min (180, gripVal + 5)
#            print 'Close', gripVal
  elif keyp == ' ':
   flVal = frVal = blVal = brVal = 90
   print ('Centre')
  elif ord(keyp) == 3:
   break
  pz.setOutput (front_left, flVal)
  pz.setOutput (front_right, frVal)
  pz.setOutput (back_left, blVal)
  pz.setOutput (back_right, brVal)

except KeyboardInterrupt:
 print

finally:
 pz.cleanup()


"""
