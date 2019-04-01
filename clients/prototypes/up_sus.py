import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

min = 115
max = 0
kit.servo[4].angle = min
kit.servo[5].angle = min
# time.sleep(2)
#kit.servo[4].angle = max
#kit.servo[5].angle = max
