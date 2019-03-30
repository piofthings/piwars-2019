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


class CannonAction:

    steeringPositions = SteeringPositions()
    __debug = False
    __position = 1
    __safety = True

    def __init__(self, isDebug=False):
        self.__debug = isDebug

    def get_command(self, position):
        cannonCommand = ""
        if(position == SteeringPositions.AIM_LASER):
            cannonCommand = '{{"cmd": "cannon","action": "aim","data": {{ "position" : {} }} }}\n'.format(
                self.__position,
            )
        elif(position == SteeringPositions.TURN_OFF_SAFETY):
            self.__safety = False
        elif(position == SteeringPositions.FIRE_CANNON):
            if(self.__safety == False):
                cannonCommand = '{{"cmd": "cannon","action": "launch","data": {{ "position" : {} }} }}\n'.format(
                    self.__position,
                )
                self.__safety = True
                if(self.__position == 5):
                    self.__position = 1
                else:
                    self.__position = self.__position + 1
        if(self.__debug == True):
            if(cannonCommand != ""):
                print(cannonCommand)
        return cannonCommand
