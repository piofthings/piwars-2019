from dc_drive import GpiozeroDrive
from keyboard_input import KeyboardInput


class KeyboardInputServices:
    __keyboardInput = None
    __looper = True

    def __init__(self):
        self.__keyboardInput = KeyboardInput("Keyboard Input Services")

    def main(self):
        while self.__looper:
