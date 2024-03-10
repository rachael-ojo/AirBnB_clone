#!/usr/bin/python3

import json


class FileStorage:

    def __init__(self, file_path):
        """Initializes a new instance of MyClass."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns all the items stored in the collection."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the collection."""
        class_name = obj.__class__.__name__
        key = class_name + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves the data associated with the object to storage."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)
