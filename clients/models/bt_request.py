import json
from serialisable_base import SerialisableBase
from bt_steering_mode_data import BtSteeringModeData
from bt_wheels_strafe_data import BtWheelsStrafeData
from bt_cannon_data import BtCannonData
from bt_suspension_data import BtSuspensionData


class BtRequest(SerialisableBase):
    cmd = ""
    action = ""
    data = None

    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)

    def deserialise(self, json_dict):
        super().deserialise(json_dict)
        if(self.data != None):
            if(self.cmd == "steering" and self.action == "move"):
                self.data = BtSteeringModeData(json_def=json.dumps(self.data))
            if(self.cmd == "wheels"):
                self.data = BtWheelsStrafeData(json_def=json.dumps(self.data))
            if(self.cmd == "cannon"):
                self.data = BtCannonData(json_def=json.dumps(self.data))
            if(self.cmd == "suspension"):
                self.data = BtCannonData(json_def=json.dumps(self.data))
