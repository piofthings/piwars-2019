#!/usr/bin/env python3
# coding: Latin-1

import time
import os
import sys
import pygame
from rock_candy import RockCandy
from pi_hut import PiHutController
from steering_positions import SteeringPositions


class JoystickInput():
    # Settings for the joystick
    __axisUpDown = 1                          # Joystick axis to read for up / down position
    # Set this to True if up and down appear to be swapped
    __axisUpDownInverted = False
    # Joystick axis to read for left / right position
    __axisLeftRight = 2
    # Set this to True if left and right appear to be swapped
    __axisLeftRightInverted = True

    # Speed to slow to when the drive slowly button is held, e.g. 0.5 would be half speed
    __slowFactor = 0.8
    # Joystick button number for driving slowly whilst held (L2)
    __buttonSlow = 6
    # Joystick button number for turning fast (R2)
    __buttonFastTurn = 7
    __leftTrigger = 0
    __kickButton = 1
    # Time between updates in seconds, smaller responds faster but uses more processor time
    __interval = 1 / 100

    __driveLeft = 0
    __driveRight = 0
    __directionLeft = 0
    __directionRight = 0
    __enabled = False

    __joystick = None

    __debug = False

    __steering_postition = SteeringPositions.NEUTRAL

    controllerButtons = PiHutController()

    @property
    def steeringPosition(self):
        """I'm the 'Steering Position' property."""
        return self.__steering_postition

    @steeringPosition.setter
    def steeringPosition(self, value):
        self.__steering_postition = value

    @property
    def driveRight(self):
        """I'm the 'driveLeft' property."""
        return self.__driveRight

    @driveRight.setter
    def driveRight(self, value):
        self.__driveRight = value

    @property
    def driveLeft(self):
        """I'm the 'driveLeft' property."""
        return self.__driveLeft

    @driveLeft.setter
    def driveLeft(self, value):
        self.__driveLeft = value

    @property
    def directionLeft(self):
        """I'm the 'driveLeft' property."""
        return self.__directionLeft

    @directionLeft.setter
    def directionLeft(self, value):
        self.__directionLeft = value

    @property
    def directionRight(self):
        """I'm the 'driveLeft' property."""
        return self.__directionRight

    @directionRight.setter
    def directionRight(self, value):
        self.__directionRight = value

    @property
    def enabled(self):
        """I'm the 'x' property."""
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

    def __init__(self, debug=False):
        # Re-direct our output to standard error, we need to ignore standard out to hide some nasty print statements from pygame
        sys.stdout = sys.stderr
        self.__debug = debug

    def init_joystick(self, start_polling=False):
        # Setup pygame and wait for the joystick to become available
        # Removes the need to have a GUI window
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.init()
        # pygame.display.set_mode((1,1))
        if(self.__debug):
            print('Waiting for joystick... (press CTRL+C to abort)')
        attempts = 0
        while attempts < 300:
            try:
                attempts = attempts + 1
                self.__connect_to_joystick()
                if(self.__joystick != None):
                    break
                time.sleep(0.1)
            except KeyboardInterrupt:
                # CTRL+C exit, give up
                if(self.__debug):
                    print('\nUser aborted')
                # sys.exit()
        if(self.__joystick != None):
            if(self.__debug):
                print('Joystick found')
            self.__joystick.init()
        else:
            if(self.__debug):
                print('Joystick not found')
        self.driveLeft = 0.0
        self.driveRight = 0.0
        running = True
        hadEvent = False
        upDown = 0.0
        leftRight = 0.0

        if (start_polling):
            self.poll_joystick_events()

    def __connect_to_joystick(self):
        try:
            pygame.joystick.init()
            # Attempt to setup the joystick
            if pygame.joystick.get_count() < 1:
                pygame.joystick.quit()
                self.__joystick = None
            else:
                # We have a joystick, attempt to initialise it!
                self.__joystick = pygame.joystick.Joystick(0)
                if(self.__debug):
                    print("Joystick found")
        except pygame.error:
            # Failed to connect to the joystick
            pygame.joystick.quit()
            self.__joystick = None

    def poll_joystick_events(self):
        if(self.__joystick == None):
            self.__connect_to_joystick()
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
                if (self.__joystick.get_button(self.controllerButtons.BUTTON_HOME)):
                    self.steeringPosition = SteeringPositions.NEUTRAL
                elif(self.__joystick.get_button(self.controllerButtons.BUTTON_R_DP_TOP)):
                    self.steeringPosition = SteeringPositions.NEUTRAL
                elif(self.__joystick.get_button(self.controllerButtons.BUTTON_R_DP_BOTTOM)):
                    self.steeringPosition = SteeringPositions.SPOT_TURN
                elif(self.__joystick.get_button(self.controllerButtons.BUTTON_R_DP_LEFT)):
                    self.steeringPosition = SteeringPositions.STRAFE_LEFT
                elif(self.__joystick.get_button(self.controllerButtons.BUTTON_R_DP_RIGHT)):
                    self.steeringPosition = SteeringPositions.STRAFE_RIGHT

                if(self.__joystick.get_button(self.controllerButtons.LEFT_TRIGGER)):
                    print(self.__joystick.get_button(self.controllerButtons.LEFT_TRIGGER))

                # Read axis positions (-1 to +1)
                if self.__axisUpDownInverted:
                    upDown = -self.__joystick.get_axis(self.__axisUpDown)
                    if(self.__debug):
                        print("going forward")
                else:
                    upDown = self.__joystick.get_axis(self.__axisUpDown)
                    if(self.__debug):
                        print("going backwards")

                if self.__axisLeftRightInverted:
                    leftRight = -self.__joystick.get_axis(self.__axisLeftRight)
                else:
                    leftRight = self.__joystick.get_axis(self.__axisLeftRight)
                # Apply steering speeds
                if not self.__joystick.get_button(self.__buttonFastTurn):
                    leftRight *= 0.5

                # Determine the drive power levels
                self.driveLeft = -upDown
                self.driveRight = -upDown
                if leftRight < -0.05:
                    # Turning left
                    self.driveLeft *= 1.0 + (2.0 * leftRight)
                elif leftRight > 0.05:
                    # Turning right
                    self.driveRight *= 1.0 - (2.0 * leftRight)
                # Check for button presses
                if self.__joystick.get_button(self.__buttonSlow):
                    self.driveLeft *= self.__slowFactor
                    self.driveRight *= self.__slowFactor
            if(self.driveRight < 0):
                self.directionRight = 0
                self.driveRight *= -1
            else:
                self.directionRight = 1

            if(self.driveLeft < 0):
                self.directionLeft = 0
                self.driveLeft *= -1
            else:
                self.directionLeft = 1


def main():
    controller = JoystickController()
    controller.init_joystick(True)


if __name__ == '__main__':
    main()
