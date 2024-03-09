#!/usr/bin/python3

from datetime import datetime
import uuid



class BaseModel:

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


    
    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)


    
    def save(self):
        """Saves the current state of the BaseModel instance."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the instance attributes into a dictionary representation."""
        dict_ionary = self.__dict__.copy()
        dict_ionary["__class__"] = type(self).__name__
        dict_ionary["created_at"] = dict_ionary["created_at"].isoformat()
        dict_ionary["updated_at"] = dict_ionary["updated_at"].isoformat()
        return dict_ionary
    

