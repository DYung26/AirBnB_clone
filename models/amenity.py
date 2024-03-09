#!/usr/bin/python3
"""
Module: amenity.py
This module defines the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing an amenity entity.

    Attributes:
        name (str): The name of the amenity.

    Note:
        The Amenity class inherits from the BaseModel class.
    """
    name = ""
