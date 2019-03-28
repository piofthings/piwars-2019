#!/usr/bin/env python3

"""
Client steering.py

"""
import math
import time
import sys
import os

from adafruit_servokit import ServoKit

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")
from steering_status import SteeringStatus
from bt_steering_mode_data import BtSteeringModeData
from bt_request import BtRequest


class Steering():
    FRONT_LEFT_POS = 1
    FRONT_RIGHT_POS = 2
    REAR_LEFT_POS = 3
    REAR_RIGHT_POS = 4

    """
    Preset Positions:
    SpotTurn:
    Front Right: 21
    Front Left:  160.7
    Rear Right: 168
    Rear Left: 75

    Strafe Left:
    Front Right: 21
    Front Left: 49.4
    Rear Right: 66.4
    Rear Left: 75

    Strafe Right:
    Front Right: 111
    Front Left: 150
    Rear Right: 168
    Rear Left: 75
    """

    steering_status = None

    __kit = None
    __Do = 0

    def __init__(self, servoKit, steeringStatusFile=None):
        self.__kit = servoKit
        if(steeringStatusFile != None):
            self.steering_status = SteeringStatus(json_file=steeringStatusFile)
            self.__frontLeftServo = self.__kit.servo[self.steering_status.front_left_port]
            self.__rearLeftServo = self.__kit.servo[self.steering_status.rear_left_port]
            self.__frontRightServo = self.__kit.servo[self.steering_status.front_right_port]
            self.__rearRightServo = self.__kit.servo[self.steering_status.rear_right_port]
            self.move_servo_to(self.FRONT_LEFT_POS, self.steering_status.front_left_start)
            self.move_servo_to(self.FRONT_RIGHT_POS, self.steering_status.front_right_start)
            self.move_servo_to(self.REAR_LEFT_POS, self.steering_status.rear_left_start)
            self.move_servo_to(self.REAR_RIGHT_POS, self.steering_status.rear_right_start)

    def spotTurn(self):
        flVal = 45
        frVal = 135
        blVal = 135
        brVal = 45
        self.__frontLeftServo.angle = blVal
        self.__rearLeftServo.angle = blVal
        self.__frontRightServo.angle = frVal
        self.__rearRightServo.angle = brVal

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

    def increment_position(self, index, increment):
        if(index == 1):
            if(self.steering_status.front_left_delta < self.steering_status.actuation_range):
                self.steering_status.front_left_delta = self.steering_status.front_left_delta + increment
                print("\r front_left_delta: " + str(self.steering_status.front_left_delta), end='\r', flush=True)
        elif(index == 2):
            if(self.steering_status.front_right_delta < self.steering_status.actuation_range):
                self.steering_status.front_right_delta = self.steering_status.front_right_delta + increment
                print("\r front_right_delta: " + str(self.steering_status.front_right_delta), end='\r', flush=True)
        elif(index == 3):
            if(self.steering_status.rear_left_delta < self.steering_status.actuation_range):
                self.steering_status.rear_left_delta = self.steering_status.rear_left_delta + increment
                print("\r rear_left_delta: " + str(self.steering_status.rear_left_delta), end='\r', flush=True)
        elif(index == 4):
            if(self.steering_status.rear_right_delta < self.steering_status.actuation_range):
                self.steering_status.rear_right_delta = self.steering_status.rear_right_delta + increment
                print("\r rear_right_delta: " + str(self.steering_status.rear_right_delta), end='\r', flush=True)

    def decrement_position(self, index, decrement):
        if(index == 1):
            if(self.steering_status.front_left_delta > 0):
                self.steering_status.front_left_delta = self.steering_status.front_left_delta - decrement
                print("\r front_left_delta: " + str(self.steering_status.front_left_delta), end='\r', flush=True)
        elif(index == 2):
            if(self.steering_status.front_right_delta > 0):
                self.steering_status.front_right_delta = self.steering_status.front_right_delta - decrement
                print("\r front_right_delta: " + str(self.steering_status.front_right_delta), end='\r', flush=True)
        elif(index == 3):
            if(self.steering_status.rear_left_delta > 0):
                self.steering_status.rear_left_delta = self.steering_status.rear_left_delta - decrement
            print("\r rear_left_delta: " + str(self.steering_status.rear_left_delta), end='\r', flush=True)
        elif(index == 4):
            if(self.steering_status.rear_right_delta > 0):
                self.steering_status.rear_right_delta = self.steering_status.rear_right_delta - decrement
                print("\r rear_right_delta: " + str(self.steering_status.rear_right_delta), end='\r', flush=True)

    def set_steering_port(self, index, value):
        if(index == 1):
            self.steering_status.front_left_port = value
        elif(index == 2):
            self.steering_status.front_right_port = value
        elif(index == 3):
            self.steering_status.rear_left_port = value
        elif(index == 4):
            self.steering_status.rear_right_port = value

    def set_actuation_degrees(self, degrees):
        if degrees < 360 and degrees > 0:
            self.steering_status.actuation_range = degrees
        self.update_servos()

    def save_steering_status(self):
        self.steering_status.front_left_delta = self.__kit.servo[int(self.steering_status.front_left_port)].angle
        self.steering_status.front_right_delta = self.__kit.servo[int(self.steering_status.front_right_port)].angle
        self.steering_status.rear_left_delta = self.__kit.servo[int(self.steering_status.rear_left_port)].angle
        self.steering_status.rear_right_delta = self.__kit.servo[int(self.steering_status.rear_right_port)].angle
        self.steering_status.save()

    def move_servo_to(self, index, value):
        if(index == 1):
            self.__kit.servo[int(self.steering_status.front_left_port)].angle = value
        elif(index == 2):
            self.__kit.servo[int(self.steering_status.front_right_port)].angle = value
        elif(index == 3):
            self.__kit.servo[int(self.steering_status.rear_left_port)].angle = value
        elif(index == 4):
            self.__kit.servo[int(self.steering_status.rear_right_port)].angle = value

    def move_servo_by(self, index, value):
        if(index == 1):
            self.__kit.servo[int(self.steering_status.front_left_port)].angle = self.__kit.servo[int(self.steering_status.front_left_port)].angle + value
            print("\r Front left servo angle: " + str(self.__kit.servo[int(self.steering_status.front_left_port)].angle), end='\r', flush=True)
        elif(index == 2):
            self.__kit.servo[int(self.steering_status.front_right_port)].angle = self.__kit.servo[int(self.steering_status.front_right_port)].angle + value

            print("\r Front right servo angle: " +
                  str(self.__kit.servo[int(self.steering_status.front_right_port)].angle), end='\r', flush=True)
        elif(index == 3):
            self.__kit.servo[int(self.steering_status.rear_left_port)
                             ].angle = self.__kit.servo[int(self.steering_status.rear_left_port)].angle + value
            print("\r Rear left servo angle: " +
                  str(self.__kit.servo[int(self.steering_status.rear_left_port)].angle), end='\r', flush=True)
        elif(index == 4):
            self.__kit.servo[int(self.steering_status.rear_right_port)].angle = self.__kit.servo[int(self.steering_status.rear_right_port)].angle + value
            print("\r Rear left right angle: " + str(self.__kit.servo[int(self.steering_status.rear_right_port)].angle), end='\r', flush=True)

    def print_servo_stats(self):
        print("Front left:" + str(self.__kit.servo[int(self.steering_status.front_left_port)].angle))
        print("Front right:" + str(self.__kit.servo[int(self.steering_status.front_right_port)].angle))
        print("Rear left:" + str(self.__kit.servo[int(self.steering_status.rear_left_port)].angle))
        print("Rear right:" + str(self.__kit.servo[int(self.steering_status.rear_right_port)].angle))

    def update_servos(self):
        self.__kit.servo[int(self.steering_status.front_left_port)].angle = self.steering_status.front_left_delta
        self.__kit.servo[int(self.steering_status.front_left_port)].actuation_range = self.steering_status.actuation_range

        self.__kit.servo[int(self.steering_status.front_right_port)].angle = self.steering_status.front_right_delta
        self.__kit.servo[int(self.steering_status.front_right_port)].actuation_range = self.steering_status.actuation_range

        self.__kit.servo[int(self.steering_status.rear_left_port)].actuation_range = self.steering_status.actuation_range

        self.__kit.servo[int(self.steering_status.rear_right_port)].angle = self.steering_status.rear_right_delta
        self.__kit.servo[int(self.steering_status.rear_right_port)].actuation_range = self.steering_status.actuation_range
