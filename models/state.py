#!/usr/bin/python3
"""State module containing the State class representing a state entity."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representing a state entity which inherits from BaseModel.

    Class Attributes:
        name (str): The name of the state."""
    name = ""
