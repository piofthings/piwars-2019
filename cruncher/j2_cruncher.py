#!/usr/bin/env python3

import atexit

from bluedot.btcomm import BluetoothServer
from signal import pause

from cruncher_menu import CruncherMenu
from cruncher_menu_option import CruncherMenuOption


class J2Cruncher:
    __bt_server = None
    __looper = True

    def __init__(sef):
        self.__bt_server = BluetoothServer(self.data_received)
        atexit.register(self.cleanup)

    def run(self):
        try:
            while __looper:
                time.sleep(1.0 / 60)
        except KeyboardInterrupt:
            self.cleanup()

    def data_received(self, data):
        print(data)
        self.__bt_server.send(data)

    def cleanup(self):
        pass
# pause()
