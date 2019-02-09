class BaseCommand(object):
    """Base Command
    Base interface providing the stop and start end points.
    Ideally each CruncherMenuOption should have a command associated.
    """
    running = False

    def __init__(self, arg):
        self.arg = arg

    def poll(self):
        running = True
        pass

    def stop(self):
        running = False
        pass
