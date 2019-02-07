#!/user/bin/python3

import json


class SerialisableBase:

    __json_file = ""

    def __init__(self, json_def, json_file):
        if json_def != None:
            s = json.loads(json_def)
            self.deserialise(s)
        if json_file != None:
            self.__json_file = json_file
            file_object = open(json_file, 'r')
            s = json.load(file_object)
            self.deserialise(s)

    def deserialise(self, json_dict):
        for field, value in json_dict.items():
            print("Field", "| Value")
            print(field, value)
            self.__dict__[
                field] = None if field not in json_dict else json_dict[field]

    def serialise(self, selfie):
        return_dict = dict()
        for field, value in selfie.__dict__.items():
            if not field.startswith('_'):
                return_dict[field] = value
        return return_dict

    def save(self, file=None):
        if file != None:
            self.__json_file = file
        if self.__json_file != None:
            file_object = open(self.__json_file, 'w+')
            s = json.dump(self, file_object, default=self.serialise)
        else:
            print(
                "Serialization error: Please provide destination either in constructor or Save")
