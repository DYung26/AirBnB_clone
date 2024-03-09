#!/usr/bin/python3
"""
Module: user.py
This module defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class which inherits from BaseModel.

    Class Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user's account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
