#!/user/bin/python3

import json


class SteeringStatus():
    front_left_delta = 0
    front_right_delta = 0
    rear_left_delta = 0
    rear_right_delta = 0

    __json_file = ""

    def __init__(self, json_def=None, json_file=None):
        if json_def != None:
            s = json.loads(json_def)
            __deserialise(s)
        if json_file != None:
            self.__json_file = json_file
            file_object = open(json_file, 'r')
            s = json.load(file_object)
            self.__deserialise(s)

    def __deserialise(self, json_dict):
        self.front_left_delta = None if 'front_left_delta' not in json_dict else json_dict[
            'front_left_delta']
        self.front_right_delta = None if 'front_right_delta' not in json_dict else json_dict[
            'front_right_delta']
        self.rear_left_delta = None if 'rear_left_delta' not in json_dict else json_dict[
            'rear_left_delta']
        self.rear_right_delta = None if 'rear_right_delta' not in json_dict else json_dict[
            'rear_right_delta']

    def __serialise(self, selfie):
        return_dict = dict(front_left_delta=selfie.front_left_delta,
                           front_right_delta=selfie.front_right_delta,
                           rear_left_delta=selfie.rear_left_delta,
                           rear_right_delta=selfie.rear_right_delta)
        return return_dict

    def Save(self):
        file_object = open(self.__json_file, 'w')
        s = json.dump(self, file_object, default=self.__serialise)
