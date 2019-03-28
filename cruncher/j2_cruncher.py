#!/usr/bin/env python3
import os
import sys
import time
import atexit
import asyncio

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))

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


class J2Cruncher:
    __bt_server = None
    __cruncher_menu = None
    __joystick_input = None
    __looper = True
    __debug = False

    def __init__(self, isDebug=False):
        self.__debug = isDebug
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
                self.process_menu()
                # if(self.__cruncher_menu.selected_command != None):
                #     self.__selected_command.start()
                self.__joystick_input.poll_joystick_events()
                self.update_j2_controller()
                await asyncio.sleep(1.0 / 60)
            except KeyboardInterrupt:
                self.__looper = False
                self.cleanup()

    def process_menu(self):
        if(self.__cruncher_menu.previous_menu_name != self.__cruncher_menu.current_menu_name):
            if(self.__cruncher_menu.current_menu_name == "ev_pi_noon"):
                self.__joystick_input.enabled = True
        # else:
            #print("Previous {}, Current {}".format(self.__cruncher_menu.previous_menu_name, self.__cruncher_menu.current_menu_name))

    def update_j2_controller(self):
        if(self.__cruncher_menu.current_menu_name == "ev_pi_noon"):
            if(self.__joystick_input.enabled == True):
                btCommand = '{{"cmd": "steering","action": "move","data": {{ "speedLeft": {},"directionLeft": {}, "speedRight": {}, "directionRight": {} }} }}'.format(
                    self.__joystick_input.driveLeft,
                    self.__joystick_input.directionLeft,
                    self.__joystick_input.driveRight,
                    self.__joystick_input.directionRight
                )
                # if(self.__joystick_input.driveRight != 0 and self.__joystick_input.driveRight != 0):
                if(self.__debug):
                    print(btCommand)
                self.__bt_server.send(btCommand)

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
