from base_command import BaseCommand
from joystick_input import JoystickController


class PiNoonCommand(BaseCommand):
    """PiNoon Command to handle Pi Noon challenge"""
    __looper = False

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def start():
        self.running = True
        self.__looper = True
        while self.__looper:
