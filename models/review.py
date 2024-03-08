#!/usr/bin/python3
"""
Module: review.py
This module defines the Review class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class representing a user's review for a place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.

    Inheritance:
        The Review class inherits from the BaseModel class.
    """
    place_id = ""
    user_id = ""
    text = ""

