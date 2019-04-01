
import time
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../libs")))

import VL53L0X


class TofSensors:
    """ Keeps track of heading using the BNO055 """
    __debug = False

    distance_left = 0
    distance_back = 0
    distance_right = 0
    distance_front = 0

    def __init__(self, isDebug=False):
        self.__debug = isDebug
        # Create a VL53L0X object for device on TCA9548A bus 1
        self.tof1 = VL53L0X.VL53L0X(TCA9548A_Num=0, TCA9548A_Addr=0x70)
        # Create a VL53L0X object for device on TCA9548A bus 2
        self.tof2 = VL53L0X.VL53L0X(TCA9548A_Num=1, TCA9548A_Addr=0x70)
        # Create a VL53L0X object for device on TCA9548A bus 3
        self.tof3 = VL53L0X.VL53L0X(TCA9548A_Num=2, TCA9548A_Addr=0x70)
        # Create a VL53L0X object for device on TCA9548A bus 4
        self.tof4 = VL53L0X.VL53L0X(TCA9548A_Num=3, TCA9548A_Addr=0x70)

    def get_sensor_values(self):

        # Start ranging on TCA9548A bus 1
        self.tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
        # Start ranging on TCA9548A bus 2
        self.tof2.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
        # Start ranging on TCA9548A bus 3
        self.tof3.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
        # Start ranging on TCA9548A bus 4
        self.tof4.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        timing = self.tof1.get_timing()
        if (timing < 20000):
            timing = 20000
        print("Timing %d ms" % (timing / 1000))

        for count in range(1, 1001):
            # Get distance from VL53L0X  on TCA9548A bus 1
            distance = self.tof1.get_distance()
            if (distance > 0):
                self.distance_left = distance
                print("Left: %d mm, %d cm, %d" % (distance, (distance / 10), count))

            # Get distance from VL53L0X  on TCA9548A bus 2
            distance = self.tof2.get_distance()
            if (distance > 0):
                self.distance_back = distance

                print("Back: %d mm, %d cm, %d" % (distance, (distance / 10), count))

            # Get distance from VL53L0X  on TCA9548A bus 3
            distance = self.tof3.get_distance()
            if (distance > 0):
                self.distance_right = distance
                print("Right: %d mm, %d cm, %d" % (distance, (distance / 10), count))

            # Get distance from VL53L0X  on TCA9548A bus 4
            distance = self.tof4.get_distance()
            if (distance > 0):
                self.distance_front = distance

                print("Front: %d mm, %d cm, %d" % (distance, (distance / 10), count))

            time.sleep(timing / 1000000.00)

        self.tof1.stop_ranging()
        self.tof2.stop_ranging()
        self.tof3.stop_ranging()
        self.tof4.stop_ranging()

        return self.distance_front, self.distance_left, self.distance_back, self.distance_right

    def save_as_start_heading(self):
        heading, roll, pitch = bno.getVector(0x1A)
