#!/usr/bin/python3

import json
class FileStorage:

    def __init__(self):
        self.__file_path = ''
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        key = class_name + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)


    def reload(self):
        pass