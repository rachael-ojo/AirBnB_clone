#!/usr/bin/python3
"""Defines a Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review."""
    
    text = ""
    user_id = ""
    place_id = ""
