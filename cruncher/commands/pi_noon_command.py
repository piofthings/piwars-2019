from base_command import BaseCommand


class PiNoonCommand(BaseCommand):
    """PiNoonCommand to handle Pi Noon challenge"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def start():
        self.running = True
