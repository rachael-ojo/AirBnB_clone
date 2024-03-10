from models.Base import Base


class Note(Base):
    """A class representing a note entity."""
    def __init__(self, **kwargs):
        """Initializes a new instance of MyClass."""
        allowedKeys = ["title", "description", "user_id", "priority"]
        super().__init__(allowedKeys, **kwargs)
