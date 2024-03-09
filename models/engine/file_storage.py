#!/usr/bin/python3

import json


class FileStorage:

    def __init__(self, file_path):

        from base_model import BaseModel

        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        
        from base_model import BaseModel
        return self.__objects

    def new(self, obj):

        from base_model import BaseModel
        class_name = obj.__class__.__name__
        key = class_name + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):

        from base_model import BaseModel
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)


    def reload(self):

        from base_model import BaseModel

        class_registry = {
    'BaseModel': BaseModel
}
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
            for key, obj_data in obj_dict.items():
                class_name = key.split(".")[0]
                cla_s = class_registry.get(class_name)
                obj = cla_s(**obj_data)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass