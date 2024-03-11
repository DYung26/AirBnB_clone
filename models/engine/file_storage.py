#!/usr/bin/python3
"""
Module: file_storage.py
This module defines the FileStorage class for managing storage of objects in
a JSON file.
"""
import json


class FileStorage:
    """
    A class for managing storage of objects in a JSON file.

    Attributes:
        __file_path (str): The file path to the JSON file.
        __objects (dict): A dictionary to store objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects stored in the storage.

        Returns:
            dict: A dictionary containing all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Saves the objects in the storage to the JSON file.
        """
        to_dump = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(to_dump))

    def reload(self):
        """
        Reloads objects from the JSON file into the storage.
        """
        # pylint: disable=import-outside-toplevel
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        cls_dicts = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.loads(f.read())
            for key, value in data.items():
                self.__objects[key] = cls_dicts[value['__class__']](**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
