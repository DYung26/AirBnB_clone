#!/usr/bin/python3
"""
Module: base_model.py
This module defines the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class represents the base model for all other classes.
    """

    def __init__(self):
        """ Initializes a new instance of the BaseModel class.

        Attributes:
            id (str): A universally unique identifier for the instance.
            created_at (datetime): The date and time when the instance was
                created.
            updated_at (datetime): The date and time when the instance was
                last updated.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a user-friendly string representation of the BaseModel
            instance.

        Returns:
            str: A string in the format '[<class name>] (<id>) <__dict__>'.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id,
            self.__dict__)

    def save(self):
        """ Updates the 'updated_at' attribute with the current date and time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Converts the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary containing all keys/values of __dict__ and
                additional properties.
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
