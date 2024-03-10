import uuid
import datetime
from models.engine.FileStorage import FileStorage
fileStorage = FileStorage()
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
