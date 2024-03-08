#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)


    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_ionary = self.__dict__.copy()
        dict_ionary["__class__"] = type(self).__name__
        dict_ionary["created_at"] = dict_ionary["created_at"].isoformat()
        dict_ionary["updated_at"] = dict_ionary["updated_at"].isoformat()
        return dict_ionary


my_base = BaseModel()
print(my_base)

my_base.save()
print("\n")
print(my_base)

my_base = my_base.to_dict()
print("\n")
print(my_base)