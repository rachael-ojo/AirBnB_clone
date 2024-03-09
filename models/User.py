from .Base import Base

class User(Base):
    def __init__(self, **kwargs):
        allowedKeys = {"username"}
        super().__init__(allowedKeys, **kwargs)