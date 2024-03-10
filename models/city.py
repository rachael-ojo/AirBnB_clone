#!/usr/bin/python3
"""Defines a city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city."""

def __init__(self, state_id, name):
    """Initializes a new instance of the Class_name with the given state_id and name."""
    self.state_id = state_id
    self.name = name
