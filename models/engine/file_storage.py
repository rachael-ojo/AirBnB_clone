#!/usr/bin/python3

import json


class FileStorage:

    def __init__(self, file_path):

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        key = class_name + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)


   