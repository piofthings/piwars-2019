#!/usr/bin/env python3
import os
import sys
import time
import atexit
import asyncio

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "actors")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "sensors/menu")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "sensors/joystick")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "commands")))

from bluedot.btcomm import BluetoothServer
from signal import pause

from cruncher_menu import CruncherMenu
from cruncher_menu_option import CruncherMenuOption
from joystick_input import JoystickInput
from steering_positions import SteeringPositions
from joystick_action import JoystickAction
from cannon_action import CannonAction


class J2Cruncher:
    __bt_server = None
    __cruncher_menu = None
    __joystick_input = None
    __looper = True
    __debug = False
    steeringPositions = SteeringPositions()
    joystick_action = None
    cannon_action = None

    def __init__(self, isDebug=False):
        self.__debug = isDebug
        self.joystick_action = JoystickAction(self.__debug)
        self.cannon_action = CannonAction(self.__debug)
        self.__bt_server = BluetoothServer(self.data_received, self.__debug)
        self.__bt_server.when_client_connects = self.bt_client_connected
        self.__bt_server.when_client_disconnects = self.bt_client_disconnected
        self.__bt_server.start()
        self.__cruncher_menu = CruncherMenu(self.__debug)
        self.__joystick_input = JoystickInput(self.__debug)
        self.__joystick_input.init_joystick()
        atexit.register(self.cleanup)
        if(self.__debug):
            print("Bluetooth Adapter Address:" + self.__bt_server.adapter.address)

    async def run(self):
        self.__cruncher_menu.init_screen()
        while self.__looper:
            try:
                self.__cruncher_menu.paint_screen()
                if(self.__cruncher_menu.previous_menu_name != self.__cruncher_menu.current_menu_name):
                    self.process_menu()
                await asyncio.sleep(1.0 / 60)
            except KeyboardInterrupt:
                self.__looper = False
                self.cleanup()

    def process_menu(self):
        if(self.__cruncher_menu.current_menu_name == "ev_pi_noon" or
                self.__cruncher_menu.current_menu_name == "ev_space_invaders"):
            self.__joystick_input.poll_joystick_events()
            self.__joystick_input.enabled = True
            self.update_j2_controller()
            if(self.__cruncher_menu.current_menu_name == "ev_space_invaders"):
                self.update_cannon_shooter()
        else:
            self.__joystick_input.enabled = False

        # else:
        #print("Previous {}, Current {}".format(self.__cruncher_menu.previous_menu_name, self.__cruncher_menu.current_menu_name))
    def update_cannon_shooter(self):
        cannonCommand = self.cannon_action.get_command(self.__joystick_input.steeringPosition)
        if(cannonCommand != ""):
            self.__bt_server.send(cannonCommand)

    def update_j2_controller(self):
        steerCommand, driveCommand = self.joystick_action.get_commands(self.__joystick_input.steeringPosition,
                                                                       self.__joystick_input.directionLeft, self.__joystick_input.driveLeft,
                                                                       self.__joystick_input.directionRight, self.__joystick_input.driveRight)

        if(steerCommand != ""):
            self.__bt_server.send(steerCommand)
        if(driveCommand != ""):
            self.__bt_server.send(driveCommand)

    def data_received(self, data):
        if(self.__debug):
            print(data)
        self.__bt_server.send(data)

    def bt_client_connected(self):
        print("Client Connected: ")

    def bt_client_disconnected(self):
        print("Client Disconnected:")

    def cleanup(self):
        self.__bt_server = None
        # pass
# pause()


if __name__ == '__main__':
    isDebug = False
    if(len(sys.argv) > 1):
        print("\n".join(sys.argv[1:]))
        if(sys.argv[1] == "debug"):
            isDebug = True

    cruncher = J2Cruncher(isDebug)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(cruncher.run())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
