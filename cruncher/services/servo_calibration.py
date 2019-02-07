
class ServoCalibration():
    """Servo Calibration service on the Cruncher"""

    def __init__(self, bt_server):
        self.__bt_server = bt_server

    def setupFrontLeft(self, data, callback):
        self.__bt_server.send()
