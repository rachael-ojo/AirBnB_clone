from models.Base import Base


class Note(Base):
    def __init__(self, **kwargs):
        allowedKeys = ["title", "description", "user_id", "priority"]
        super().__init__(allowedKeys, **kwargs)