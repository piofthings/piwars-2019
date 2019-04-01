import sys
import time
import math
import traceback
from math import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../services")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../actors")))

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../libs")))

from pixy import *
from ctypes import *
from blocks import Blocks
from vector import Vector

pixy.init()
pixy.change_prog("line")


class Vector (Structure):
    _fields_ = [
        ("m_x0", c_uint),
        ("m_y0", c_uint),
        ("m_x1", c_uint),
        ("m_y1", c_uint),
        ("m_index", c_uint),
        ("m_flags", c_uint)]


class IntersectionLine (Structure):
    _fields_ = [
        ("m_index", c_uint),
        ("m_reserved", c_uint),
        ("m_angle", c_uint)]


class PixyLineSensor:
    def __init__(self):
        self.vectors = VectorArray(100)
        self.intersections = IntersectionLineArray(100)
        self.frame = 0

    def sense(self):
        line_get_all_features()
        #i_count = line_get_intersections(100, self.intersections)
        v_count = line_get_vectors(100, self.vectors)

        if v_count > 0:
            # for index in range(0, i_count):
            #     print '[INTERSECTION: INDEX=%d ANGLE=%d]' % (intersections[index].m_index, intersections[index].m_angle)
            for index in range(0, v_count):
                print '[VECTOR: INDEX=%d X0=%3d Y0=%3d X1=%3d Y1=%3d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, vectors[index].m_x1, vectors[index].m_y1)
                currentVector = vectors[index]
                vectorWidth = abs(currentVector.m_x0 - currentVector.m_x1)
                vectorHeight = abs(currentVector.m_y0 - currentVector.m_y1)
                angle = degree(atan(vectorHeight / vectorWidth))
                if(angle > 5):
                    if(currentVector.m_x0 > currentVector.m_x1):
                        # going right
                        pass
                    else:
                        # going left
                        pass


"""
# Front Left wheel:
    1. Zeroes at : 104.45
    2. To go Left : Increase angle in degrees
    3. To go Right: Decrease angle in degrees

# Front Right wheel:
    1. Zeroes at : 73.42
    2. To go Left: Decrease angle in degrees
    3. To go Right: Increase angle in degrees

# Rear Left wheel:
    1. Zeroes at : 143.106
    2. To go left : Decrease angle in degress
    3. To go right: Increase angle in degrees

# Rear Right Wheel:
    1. Zeros at:  11.48
    2. To go left: Increase angle in degrees
    3. To go right: Decrease angle in degrees

"""
