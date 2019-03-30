
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../libs")))

from BNO055 import BNO055


class HeadingSensor:
    """ Keeps track of heading using the BNO055 """
    __imu = BNO055()
    __debug = False

    def __init__(self, isDebug=False):
        self.__debug = isDebug
        if not self.__imu.begin():
            raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

    def get_heading(self):
        heading, roll, pitch = bno.getVector(0x1A)
        return heading

    def save_as_start_heading(self):
        heading, roll, pitch = bno.getVector(0x1A)
