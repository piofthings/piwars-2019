import json
from serialisable_base import SerialisableBase


class BtWheelsStrafeData(SerialisableBase):
    frontLeftAngle = "0.0"
    frontRightAngle = "0.0"
    rearLeftAngle = "0.0"
    rearRightAngle = "0.0"

    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)

    def deserialise(self, json_dict):
        super().deserialise(json_dict)
