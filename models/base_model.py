#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        
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
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)


    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_ionary = self.__dict__.copy()
        dict_ionary["__class__"] = type(self).__name__
        dict_ionary["created_at"] = dict_ionary["created_at"].isoformat()
        dict_ionary["updated_at"] = dict_ionary["updated_at"].isoformat()
        return dict_ionary
    

mudis_model = BaseModel()
mudis_model.name = "Mudi"
mudis_model.id_number = 150
mudis_model.school = "Alx SE"

dict_mudis_model = mudis_model.to_dict()

print(dict_mudis_model)

print("\n")

# creating a new BaseModel instance from the dictionary

rachael_model = BaseModel(**dict_mudis_model)

print("Original model: ", mudis_model.name, mudis_model.school)
print("\n")
print("New model: ", rachael_model.name, rachael_model.school)

print("\n")

print("Original model: ", mudis_model)
print("\n")
print("New model: ", rachael_model)

print("\n")

print("Type of original created_at: ", type(mudis_model.created_at))
print("Type of new created_at: ", type(rachael_model.created_at))


