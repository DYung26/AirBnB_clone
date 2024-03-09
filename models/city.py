#!/usr/bin/python3
"""
Module: city.py
This module defines the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city entity.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state to which the city belongs.

    Note:
        The City class inherits from the BaseModel class.
    """
    name = ""
    state_id = ""
