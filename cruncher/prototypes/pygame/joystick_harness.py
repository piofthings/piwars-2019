#!/usr/bin/env python3
# coding: Latin-1

import time
import os
import sys
import pygame
from rock_candy import RockCandy
from pi_hut import PiHutController
from steering_positions import SteeringPositions

__looper = True
# Setup pygame and wait for the joystick to become available

print('Waiting for joystick... (press CTRL+C to abort)')
attempts = 0


while attempts < 300:
    try:
        attempts = attempts + 1
        pygame.joystick.init()
        # Attempt to setup the joystick
        if pygame.joystick.get_count() < 1:
            pygame.joystick.quit()
            __joystick = None
        else:
            # We have a joystick, attempt to initialise it!
            __joystick = pygame.joystick.Joystick(0)
            print("Joystick found")
            break
    except pygame.error:
        # Failed to connect to the joystick
        pygame.joystick.quit()
        __joystick = None
        if(__joystick != None):
            break
        time.sleep(0.1)
    except KeyboardInterrupt:
        # CTRL+C exit, give up
        print('\nUser aborted')
        sys.exit()
if(__joystick != None):
    print('Joystick found')
    __joystick.init()
else:
    print('Joystick not found')

driveLeft = 0.0
driveRight = 0.0
running = True
hadEvent = False
upDown = 0.0
leftRight = 0.0

controllerButtons = PiHutController()

# Removes the need to have a GUI window
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
#pygame.display.set_mode((1,1))
while __looper:
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
            if (__joystick.get_button(controllerButtons.BUTTON_HOME)):
                steeringPosition = SteeringPositions.NEUTRAL
                print("controllerButtons.BUTTON_HOME")
            elif(__joystick.get_button(controllerButtons.BUTTON_R_DP_TOP)):
                steeringPosition = SteeringPositions.NEUTRAL
                print("controllerButtons.BUTTON_R_DP_TOP")

            elif(__joystick.get_button(controllerButtons.BUTTON_R_DP_BOTTOM)):
                steeringPosition = SteeringPositions.SPOT_TURN
                print("controllerButtons.BUTTON_R_DP_BOTTOM")

            elif(__joystick.get_button(controllerButtons.BUTTON_R_DP_LEFT)):
                steeringPosition = SteeringPositions.STRAFE_LEFT
                print("controllerButtons.BUTTON_R_DP_LEFT")

            elif(__joystick.get_button(controllerButtons.BUTTON_R_DP_RIGHT)):
                steeringPosition = SteeringPositions.STRAFE_RIGHT
                print("controllerButtons.BUTTON_R_DP_RIGHT")

            elif(__joystick.get_button(controllerButtons.LEFT_TRIGGER)):
                steeringPosition = SteeringPositions.AIM_LASER
                print("controllerButtons.LEFT_TRIGGER")

            elif(__joystick.get_button(controllerButtons.RIGHT_TRIGGER)):
                steeringPosition = SteeringPositions.FIRE_CANNON
                print("controllerButtons.RIGHT_TRIGGER")

            elif(__joystick.get_button(controllerButtons.BUTTON_SELECT)):
                steeringPosition = SteeringPositions.TURN_OFF_SAFETY
                print("controllerButtons.BUTTON_SELECT")

            # Read axis positions (-1 to +1)
            upDown = -__joystick.get_axis(controllerButtons.L_JS_UP_DOWN)
            print("controllerButtons.L_JS_UP_DOWN" +str(upDown))
            leftRight = -__joystick.get_axis(controllerButtons.L_JS_LEFT_RIGHT)
            print("controllerButtons.L_JS_LEFT_RIGHT" +str(leftRight))
