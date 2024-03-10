#!/usr/bin/python3
from datetime import Datetime
import uuid
<<<<<<< HEAD

=======
import datetime
from models.engine.FileStorage import FileStorage
fileStorage = FileStorage()
>>>>>>> fc3446b10f8326920553a111899f12c057dcfcd1
class Base:
    """A class representing a note entity."""
    def __init__(self, **kwargs):
        """Initializes a new instance of MyClass."""
        self.__dict__ = kwargs
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        fileStorage.create(self)


    def __str__(self):
        """Returns a string representation of the object."""
        return f"{self.__dict__}"
