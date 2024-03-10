#!/usr/bin/python3
"""Defines a Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place."""

    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    number_rooms = 0
    name = ""
    max_guest = 0
    city_id = ""
    number_bathrooms = 0
    user_id = ""
    description = ""
