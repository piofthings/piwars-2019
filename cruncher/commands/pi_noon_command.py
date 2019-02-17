from base_command import BaseCommand
from joystick_input import JoystickInput


class PiNoonCommand(BaseCommand):
    """PiNoon Command to handle Pi Noon challenge"""
    __joystick_input = None

    def __init__(self, arg=None):
        super().__init__()
        self.arg = arg
        self.__joystick_input = JoystickInput()

    def poll(self):
        self.running = True
        self.__joystick_input.run()
