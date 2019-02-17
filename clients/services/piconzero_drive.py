#!/usr/bin/env python3

import piconzero as pz
import time
from time import sleep


class PiconzeroDrive():
    DIRECTION_FORWARD = 1
    DIRECTION_BACKWARD = 0

    __currentLeftDirection = DIRECTION_FORWARD
    __currentRightDirection = DIRECTION_FORWARD
    __currentSpeed = 0

    def __init__(self):
        pz.init()

    def setDirection(self, leftDirection, rightDirection):
        self.__currentLeftDirection = leftDirection
        self.__currentRightDirection = rightDirection

    def moveForward(self, newSpeed):
        if newSpeed >= 0 and newSpeed <= 1:
            self.setDirection(self.DIRECTION_FORWARD, self.DIRECTION_FORWARD)
            pz.forward(speed)

    def moveBackward(self, newSpeed):
        if newSpeed >= 0 and newSpeed <= 1:
            self.setSpeed(self.DIRECTION_BACKWARD, self.DIRECTION_BACKWARD)
            pz.reverse(speed)

    def move(self, directionLeft, directionRight, speedLeft, speedRight):
        self.setDirection(directionLeft, directionRight)
        if (speedLeft >= 0 and speedRight >= 0 and
                speedLeft <= 1 and speedRight <= 1):
            if(directionLeft == self.DIRECTION_FORWARD):
                print("Forward Left {}, {}".format(directionLeft, speedLeft * 123))
                pz.setMotor(0, int(speedLeft * 123))
            elif(directionLeft == self.DIRECTION_BACKWARD):
                print("Backward Left {}, {}".format(directionLeft, -1 * speedLeft * 123))
                pz.setMotor(0, int(-1 * speedLeft * 123))

            if(directionRight == self.DIRECTION_FORWARD):
                print("Forward Right {}, {}".format(directionRight, speedRight * 123))
                pz.setMotor(1, int(speedRight * 123))
            elif(directionRight == self.DIRECTION_BACKWARD):
                print("Backward Right {}, {}".format(directionRight, -1 * speedRight * 123))
                pz.setMotor(1, int(-1 * speedRight * 123))
        else:
            print("Invalid values")

    def stop(self):
        self.setSpeed(0)
        pz.stop(0)

    def cleanup(self):
        pz.stop()
        pz.cleanup()
