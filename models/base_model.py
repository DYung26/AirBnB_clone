#!/usr/bin/python3
"""
Module: base_model.py
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class represents the base model for all other classes.
    """

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of the BaseModel class.

        Attributes:
            arg (tuple): arguments
            kwargs (dict): keywords arguments
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    setattr(self, 'created_at', datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                    continue
                if key == 'updated_at':
                    setattr(self, 'updated_at', datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                    continue
                setattr(self, key, value)

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
