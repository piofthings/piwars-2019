#!/usr/bin/env python3

from gpiozero import PhaseEnableMotor
from time import sleep


class GpiozeroDrive():
    DIRECTION_FORWARD = 1
    DIRECTION_BACKWARD = 0

    __pwmEnablePinWhiteLeftChannel = 12
    __phaseDirPinRedLeftChannel = 5
    __pwmEnablePinWhiteRightChannel = 13
    __phaseDirPinRedRightChannel = 6

    __rightMotors = PhaseEnableMotor(
        phase=__phaseDirPinRedLeftChannel, enable=__pwmEnablePinWhiteLeftChannel, pwm=True)
    __leftMotors = PhaseEnableMotor(
        phase=__phaseDirPinRedRightChannel, enable=__pwmEnablePinWhiteRightChannel, pwm=True)

    __currentSpeed = 0

    def setDirection(self, leftDirection, rightDirection):
        self.__currentLeftDirection = leftDirection
        self.__currentRightDirection = rightDirection

    def moveForward(self, newSpeed):
        if newSpeed >= 0 and newSpeed <= 1:
            self.setDirection(self.DIRECTION_FORWARD, self.DIRECTION_FORWARD)
            self.__rightMotors.forward(speed)
            self.__leftMotors.forward(speed)

    def moveBackward(self, newSpeed):
        if newSpeed >= 0 and newSpeed <= 1:
            self.setSpeed(self.DIRECTION_BACKWARD, self.DIRECTION_BACKWARD)
            self.__rightMotors.backward(speed)
            self.__leftMotors.backward(speed)

    def move(self, directionLeft, directionRight, speedLeft, speedRight):
        self.setDirection(directionLeft, directionRight)
        if (speedLeft >= 0 and speedRight >= 0 and
                speedLeft <= 1 and speedRight <= 1):
            if(directionLeft == self.DIRECTION_FORWARD):
                self.__leftMotors.forward(speedLeft)
            elif(directionLeft == self.DIRECTION_BACKWARD):
                self.__leftMotors.backward(speedLeft)

            if(directionRight == self.DIRECTION_FORWARD):
                self.__rightMotors.forward(speedRight)
            elif(directionRight == self.DIRECTION_BACKWARD):
                self.__rightMotors.backward(speedRight)

    def stop(self):
        self.setSpeed(0)
        self.__rightMotors.forward(0)
        self.__leftMotors.forward(0)


"""
enable_pwm_white_02 =  12
phase_dir_red_02 = 5
enable_pwm_white_01 = 13
phase_dir_red_01 = 6

motor = PhaseEnableMotor(phase=phase_dir_red_02, enable=enable_pwm_white_02, pwm=True)
motor1 = PhaseEnableMotor(phase=phase_dir_red_01, enable=enable_pwm_white_01, pwm=True)

count = 0
speed = 50/100
while count < 100:
	count = count + 1
	if count < 100:
		#speed = count * 2 / 100
		motor1.forward(speed)
		motor.backward(speed)
	#elif count == 50:
		#speed = 0
	#else :
		#speed = (count * 2 - 100) / 100
		#motor.backward(speed)
		#motor1.backward(speed)
	print("speed: " + str(speed))
	sleep(0.25)
    """
