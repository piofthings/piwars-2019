#!/user/bin/python3

import json
from serialisable_base import SerialisableBase


class SteeringStatus(SerialisableBase):
    front_left_port = -1
    front_right_port = -1
    rear_left_port = -1
    rear_right_port = -1
    front_left_delta = 0
    front_right_delta = 0
    rear_left_delta = 0
    rear_right_delta = 0
    front_right_start = 135
    front_left_start = 135
    rear_left_start = 135
    rear_right_start = 135
    actuation_range = 180

    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)
