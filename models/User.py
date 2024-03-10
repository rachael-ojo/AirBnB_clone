from .Base import Base

class User(Base):
    """A class representing a user entity."""
    def __init__(self, **kwargs):
        """Initializes a new instance of MyClass."""
        allowedKeys = {"username"}
        super().__init__(allowedKeys, **kwargs)
