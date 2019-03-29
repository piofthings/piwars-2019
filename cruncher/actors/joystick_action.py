#!/usr/bin/env python3
import os
import sys
import time
import atexit
import asyncio

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../sensors/menu")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../sensors/joystick")))

from steering_positions import SteeringPositions


class JoystickAction:
    """Converts Joystick values into actionable commands for Controller"""

    steeringPositions = SteeringPositions()
    __debug = False

    def __init__(self, isDebug=False):
        self.__debug = isDebug

    def get_commands(self, joystick_steering_position, dirLeft, driveLeft, dirRight, driveRight):
        steerCommand = ""
        if(joystick_steering_position == SteeringPositions.NEUTRAL):
            steerCommand = '{{"cmd": "wheels","action": "strafe","data": {{ "frontLeftAngle" : {}, "frontRightAngle" : {}, "rearLeftAngle" : {}, "rearRightAngle": {} }} }}\n'.format(
                self.steeringPositions.defaults[SteeringPositions.NEUTRAL][0],
                self.steeringPositions.defaults[SteeringPositions.NEUTRAL][1],
                self.steeringPositions.defaults[SteeringPositions.NEUTRAL][2],
                self.steeringPositions.defaults[SteeringPositions.NEUTRAL][3]
            )
        elif(joystick_steering_position == SteeringPositions.STRAFE_LEFT):
            steerCommand = '{{"cmd": "wheels","action": "strafe","data": {{ "frontLeftAngle" : {}, "frontRightAngle" : {}, "rearLeftAngle" : {}, "rearRightAngle": {} }} }}\n'.format(
                self.steeringPositions.defaults[SteeringPositions.STRAFE_LEFT][0],
                self.steeringPositions.defaults[SteeringPositions.STRAFE_LEFT][1],
                self.steeringPositions.defaults[SteeringPositions.STRAFE_LEFT][2],
                self.steeringPositions.defaults[SteeringPositions.STRAFE_LEFT][3]
            )
        elif(joystick_steering_position == SteeringPositions.STRAFE_RIGHT):
            steerCommand = '{{"cmd": "wheels","action": "strafe","data": {{ "frontLeftAngle" : {}, "frontRightAngle" : {}, "rearLeftAngle" : {}, "rearRightAngle": {} }} }}\n'.format(
                self.steeringPositions.defaults[SteeringPositions.STRAFE_RIGHT][0],
                self.steeringPositions.defaults[SteeringPositions.STRAFE_RIGHT][1],
                self.steeringPositions.defaults[SteeringPositions.STRAFE_RIGHT][2],
                self.steeringPositions.defaults[SteeringPositions.STRAFE_RIGHT][3]
            )
        elif(joystick_steering_position == SteeringPositions.SPOT_TURN):
            if(self.__debug):
                print("SPOT TURN: " + steerCommand)
            steerCommand = '{{"cmd": "wheels","action": "strafe","data": {{ "frontLeftAngle" : {}, "frontRightAngle" : {}, "rearLeftAngle" : {}, "rearRightAngle": {} }} }}\n'.format(
                self.steeringPositions.defaults[SteeringPositions.SPOT_TURN][0],
                self.steeringPositions.defaults[SteeringPositions.SPOT_TURN][1],
                self.steeringPositions.defaults[SteeringPositions.SPOT_TURN][2],
                self.steeringPositions.defaults[SteeringPositions.SPOT_TURN][3]
            )

        if(joystick_steering_position == SteeringPositions.NEUTRAL):
            driveCommand = '{{"cmd": "steering","action": "move","data": {{ "speedLeft": {},"directionLeft": {}, "speedRight": {}, "directionRight": {} }} }}\n'.format(
                driveLeft,
                dirLeft,
                driveRight,
                dirRight)
        elif(joystick_steering_position == SteeringPositions.STRAFE_LEFT):
            driveCommand = '{{"cmd": "steering","action": "move","data": {{ "speedLeft": {},"directionLeft": {}, "speedRight": {}, "directionRight": {} }} }}\n'.format(
                driveLeft,
                dirLeft,
                driveLeft,
                dirLeft)
        elif(joystick_steering_position == SteeringPositions.STRAFE_RIGHT):
            driveCommand = '{{"cmd": "steering","action": "move","data": {{ "speedLeft": {},"directionLeft": {}, "speedRight": {}, "directionRight": {} }} }}\n'.format(
                driveRight,
                dirRight,
                driveRight,
                dirRight)
        elif(joystick_steering_position == SteeringPositions.SPOT_TURN):
            dirLeft = dirRight
            if(dirRight == 0):
                dirLeft = 1
            else:
                dirLeft = 0

        driveCommand = '{{"cmd": "steering","action": "move","data": {{ "speedLeft": {},"directionLeft": {}, "speedRight": {}, "directionRight": {} }} }}\n'.format(
            driveRight,
            dirLeft,
            driveRight,
            dirRight)
        if(self.__debug):
            # print(driveCommand)
            pass
        return steerCommand, driveCommand
