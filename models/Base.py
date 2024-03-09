import uuid
import datetime
class Base:
    def __init__(self, allowedKeys, **kwargs):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        print("the kwargs is", kwargs)
        for key in kwargs:
            if key in allowedKeys:
                self.__dict__[key] = kwargs[key]

    def __str__(self):
        return f"{self.__dict__}"


