#!/usr/bin/python3
from datetime import Datetime
import uuid

class Base:
    """A class representing a note entity."""
    def __init__(self, allowedKeys, **kwargs):
        """Initializes a new instance of MyClass."""
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        print("the kwargs is", kwargs)
        for key in kwargs:
            if key in allowedKeys:
                self.__dict__[key] = kwargs[key]

    def __str__(self):
        """Returns a string representation of the object."""
        return f"{self.__dict__}"
