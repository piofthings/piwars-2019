import json
from serialisable_base import SerialisableBase


class BtRequest(SerialisableBase):
    cmd = ""
    action = ""
    data = None

    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)
