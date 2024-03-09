from models.Note import Note
from models.User import User


# def my_fun(**kwargs):
#     for key in kwargs:
#         print (key, kwargs[key])


a = {"Amanuel": 100, "ALX": 200}
user = User(**{"username": "Amanuel", "password": "123456"})
note = Note(**{"title": "Note Title", "description": "note description"})
