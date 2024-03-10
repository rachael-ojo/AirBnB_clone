#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if kwargs:
            for ky, val in kwargs.items():
                if ky == 'created_at' or ky == 'updated_at':
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if ky != '__class__':
                    setattr(self, ky, val)
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            
        else:
            models.storage.new(self)
    
    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
    
    def save(self):
        """Saves the current state of the BaseModel instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts the instance attributes into a dictionary representation."""
        dict_ionary = self.__dict__.copy()
        dict_ionary["__class__"] = type(self).__name__
        dict_ionary["created_at"] = dict_ionary["created_at"].isoformat()
        dict_ionary["updated_at"] = dict_ionary["updated_at"].isoformat()
        return dict_ionary
