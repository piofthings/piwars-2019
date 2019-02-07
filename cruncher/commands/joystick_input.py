#!/usr/bin/env python3
# coding: Latin-1

import time
import os
import sys
import pygame


class JoystickController():
    # Settings for the joystick
    __axisUpDown = 1                          # Joystick axis to read for up / down position
    # Set this to True if up and down appear to be swapped
    __axisUpDownInverted = False
    # Joystick axis to read for left / right position
    __axisLeftRight = 2
    # Set this to True if left and right appear to be swapped
    __axisLeftRightInverted = False

    # Speed to slow to when the drive slowly button is held, e.g. 0.5 would be half speed
    __slowFactor = 0.5
    # Joystick button number for driving slowly whilst held (L2)
    __axisLeftRightInverted = 6
    # Joystick button number for turning fast (R2)
    __buttonFastTurn = 7
    __leftTrigger = 0
    __kickButton = 1
    # Time between updates in seconds, smaller responds faster but uses more processor time
    __interval = 1 / 100

    def __init__(self):
        # Re-direct our output to standard error, we need to ignore standard out to hide some nasty print statements from pygame
        sys.stdout = sys.stderr

    def run(self):
        # Setup pygame and wait for the joystick to become available
        # Removes the need to have a GUI window
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.init()
        # pygame.display.set_mode((1,1))
        print('Waiting for joystick... (press CTRL+C to abort)')
        while True:
            try:
                try:
                    pygame.joystick.init()
                    # Attempt to setup the joystick
                    if pygame.joystick.get_count() < 1:
                        # No joystick attached, set LEDs blue
                        # self.__tb.SetLeds(0, 0, 1)
                        pygame.joystick.quit()
                        time.sleep(0.1)
                    else:
                        # We have a joystick, attempt to initialise it!
                        joystick = pygame.joystick.Joystick(0)
                        break
                except pygame.error:
                    # Failed to connect to the joystick, set LEDs blue
                    pygame.joystick.quit()
                    time.sleep(0.1)
            except KeyboardInterrupt:
                # CTRL+C exit, give up
                print('\nUser aborted')
                sys.exit()
        print('Joystick found')
        joystick.init()
        ledBatteryMode = True
        try:
            print('Press CTRL+C to quit')
            driveLeft = 0.0
            driveRight = 0.0
            running = True
            hadEvent = False
            upDown = 0.0
            leftRight = 0.0
            # Loop indefinitely
            while running:
                # Get the latest events from the system
                hadEvent = False
                events = pygame.event.get()
                # Handle each event individually
                for event in events:
                    if event.type == pygame.QUIT:
                        # User exit
                        running = False
                    elif event.type == pygame.JOYBUTTONDOWN:
                        # A button on the joystick just got pushed down
                        hadEvent = True
                    elif event.type == pygame.JOYBUTTONUP:
                        # A button on the joystick just got pushed down
                        releaseEvent = True
                    elif event.type == pygame.JOYAXISMOTION:
                        # A joystick has been moved
                        hadEvent = True
                    if hadEvent:
                        if(joystick.get_button(self.__leftTrigger)):
                            print(joystick.get_button(self.__leftTrigger))
                            self.__ub.SetServoPosition3(-0.6)
                        if(joystick.get_button(self.__kickButton)):
                            self.__ub.SetServoPosition3(0.7)
                        # Read axis positions (-1 to +1)
                        if self.__axisUpDownInverted:
                            upDown = -joystick.get_axis(self.__axisUpDown)
                        else:
                            upDown = joystick.get_axis(self.__axisUpDown)
                        if self.__axisLeftRightInverted:
                            leftRight = -joystick.get_axis(self.__axisLeftRight)
                        else:
                            leftRight = joystick.get_axis(self.__axisLeftRight)
                        # Apply steering speeds
                        if not joystick.get_button(self.__buttonFastTurn):
                            leftRight *= 0.5

                        # Determine the drive power levels
                        driveLeft = -upDown
                        driveRight = -upDown
                        if leftRight < -0.05:
                            # Turning left
                            driveLeft *= 1.0 + (2.0 * leftRight)
                        elif leftRight > 0.05:
                            # Turning right
                            driveRight *= 1.0 - (2.0 * leftRight)
                        # Check for button presses
                        if joystick.get_button(self.__axisLeftRightInverted):
                            driveLeft *= self.__slowFactor
                            driveRight *= self.__slowFactor
                        # Set the motors to the new speeds
                        # self.__tb.SetMotor1(driveRight * self.maxPower)
                        # self.__tb.SetMotor2(driveLeft * self.maxPower)
                # Wait for the __interval period
                time.sleep(self.__interval)
            # Disable all drives
            # self.__tb.MotorsOff()
        except KeyboardInterrupt:
            # CTRL+C exit, disable all drives
            # self.__tb.MotorsOff()
            # self.__tb.SetCommsFailsafe(False)
            # self.__tb.SetLedShowBattery(False)
            # self.__tb.SetLeds(0, 0, 0)
        print

    def init_main():
        # self.__tb.Init()
        # self.__ub.Init()


def main():
    # tb = ThunderBorg3.ThunderBorg()
    dc = DcDrive()
    controller = JoystickController(tb, ub)
    controller.init_main()
    controller.run()


if __name__ == '__main__':
    main()
