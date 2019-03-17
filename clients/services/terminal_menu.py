import sys
import os
from keyboard_input import KeyboardInput


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "models")))


class TerminalMenu():
    __keyboardInput = KeyboardInput("J2Controller")
    keyPress = None

    def __init__(self):
        pass

    def menu(self):
        self.__keyboardInput.clear()
        print("J2 Controller")
        print("Press <Esc> or Ctrl-C to exit")
        print("c: Wheel Calibration")
        print("d: Test drive")
        print("--------------------")
        print("q: Quit")
        print("")
        keyPress = self.__keyboardInput.readkey()
        return keyPress
