#!/usr/bin/env python3
import os
import sys
import time
import atexit

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))

from bluedot.btcomm import BluetoothServer
from signal import pause

from cruncher_menu import CruncherMenu
from cruncher_menu_option import CruncherMenuOption


class J2Cruncher:
    __bt_server = None
    __cruncher_menu = None
    __looper = True

    def __init__(sef):
        self.__bt_server = BluetoothServer(self.data_received)
        self.__cruncher_menu = CruncherMenu()
        atexit.register(self.cleanup)

    def run(self):
        self.__cruncher_menu.init_screen()
        try:
            while __looper:
                self.__cruncher_menu.paint_screen()
                # if(self.__cruncher_menu.selected_command != None):
                #     self.__selected_command.start()
                time.sleep(1.0 / 60)
        except KeyboardInterrupt:
            self.cleanup()

    def data_received(self, data):
        print(data)
        self.__bt_server.send(data)

    def cleanup(self):
        self.__bt_server = None
        pass
# pause()
