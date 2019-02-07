import json
from serialisable_base import SerialisableBase


class BtCommand(SerialisableBase):
    cmd = ""
    action = ""
    data = ""

    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)
