
#!/usr/bin/python

# MIT License
#
# Copyright (c) 2017 John Bryan Moore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X

# Create a VL53L0X object for device on TCA9548A bus 1
tof1 = VL53L0X.VL53L0X(TCA9548A_Num=0, TCA9548A_Addr=0x70)
# Create a VL53L0X object for device on TCA9548A bus 2
tof2 = VL53L0X.VL53L0X(TCA9548A_Num=1, TCA9548A_Addr=0x70)
# Create a VL53L0X object for device on TCA9548A bus 3
tof3 = VL53L0X.VL53L0X(TCA9548A_Num=2, TCA9548A_Addr=0x70)
# Create a VL53L0X object for device on TCA9548A bus 4
tof4 = VL53L0X.VL53L0X(TCA9548A_Num=3, TCA9548A_Addr=0x70)

# Start ranging on TCA9548A bus 1
tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
# Start ranging on TCA9548A bus 2
tof2.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
# Start ranging on TCA9548A bus 3
tof3.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
# Start ranging on TCA9548A bus 4
tof4.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof1.get_timing()
if (timing < 20000):
    timing = 20000
print("Timing %d ms" % (timing / 1000))

for count in range(1, 1001):
    # Get distance from VL53L0X  on TCA9548A bus 1
    distance = tof1.get_distance()
    if (distance > 0):
        print("Left: %d mm, %d cm, %d" % (distance, (distance / 10), count))

    # Get distance from VL53L0X  on TCA9548A bus 2
    distance = tof2.get_distance()
    if (distance > 0):
        print("Back: %d mm, %d cm, %d" % (distance, (distance / 10), count))

    # Get distance from VL53L0X  on TCA9548A bus 3
    distance = tof3.get_distance()
    if (distance > 0):
        print("Right: %d mm, %d cm, %d" % (distance, (distance / 10), count))

    # Get distance from VL53L0X  on TCA9548A bus 4
    distance = tof4.get_distance()
    if (distance > 0):
        print("Front: %d mm, %d cm, %d" % (distance, (distance / 10), count))

    time.sleep(timing / 1000000.00)

tof1.stop_ranging()
tof2.stop_ranging()
tof3.stop_ranging()
tof4.stop_ranging()
