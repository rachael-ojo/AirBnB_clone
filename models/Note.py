from models.Base import Base


class Note(Base):
    """A class representing a note entity."""
    def __init__(self, **kwargs):
        """Initializes a new instance of MyClass."""
        super().__init__(**kwargs)
