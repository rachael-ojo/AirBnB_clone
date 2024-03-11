#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine."""

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

    def classes(self):
        """  """
        classes = {"Amenity": Amenity,
                   "BaseModel": BaseException,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "State": State,
                   "User": User}
        return classes
    
    def reload(self):
        """  """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            print(f"File {FileStorage.__file_path} not found.")

            FileStorage.__objects = {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {FileStorage.__file_path}: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        def attributes(self):
            """Returns the valid attributes and their types for classname"""
            attributes = {
                "BaseModel":
                        {"id": str,
                        "created_at": datetime.datetime,
                        "updated_at": datetime.datetime},
                "User":
                        {"email": str,
                        "password": str,
                        "first_name": str,
                        "last_name": str},
                "State":
                        {"name": str},
                "City":
                        {"state_id": str,
                        "name": str},
                "Amenity":
                        {"name": str},
                "Place":
                        {"city_id": str,
                        "user_id": str,
                        "name": str,
                        "description": str,
                        "number_rooms": int,
                        "number_bathrooms": int,
                        "max_guest": int,
                        "price_by_night": int,
                        "latitude": float,
                        "longitude": float,
                        "amenity_ids": list},
                "Review":
                {"place_id": str,
                            "user_id": str,
                            "text": str}
            }
            return attributes
