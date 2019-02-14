#!/usr/bin/env python3

import piconzero as pz
from time import sleep


class PiconzeroDrive():
    DIRECTION_FORWARD = 1
    DIRECTION_BACKWARD = 0

    __currentLeftDirection = DIRECTION_FORWARD
    __currentRightDirection = DIRECTION_FORWARD
    __currentSpeed = 0

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
        if (speedLeft >= 0 & & speedRight >= 0 & &
                speedLeft <= 1 & & speedRight <= 1):
            if(directionLeft == self.DIRECTION_FORWARD):
                pz.setMotor(0, speedLeft * 100)
            elif(directionLeft == self.DIRECTION_BACKWARD)
                pz.setMotor(0, -1 * speedLeft * 100)

            if(directionRight == self.DIRECTION_FORWARD)
                pz.setMotor(1, speedRight * 100)
            elif(directionRight == self.DIRECTION_BACKWARD):
                pz.setMotor(1, -1 * speedRight * 100)

    def stop(self):
        self.setSpeed(0)
        pz.stop(0)
