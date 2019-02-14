import json
from serialisable_base import SerialisableBase
from bt_steering_mode_data import BtSteeringModeData


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
