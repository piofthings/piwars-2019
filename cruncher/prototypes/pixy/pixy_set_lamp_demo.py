import pixy
import time
from ctypes import *
from pixy import *

# Pixy2 Python SWIG Set Lamp Example #

print ("Pixy2 Python SWIG Example -- Set Lamp")

pixy.init ()
pixy.change_prog ("video")

pixy.set_lamp (1, 0)
time.sleep(5)
pixy.set_lamp (0, 1)
