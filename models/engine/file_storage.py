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
        obj_copy = self.__objects.copy()
        to_dump = {key: value.to_dict() for key, value in obj_copy.items()}
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(to_dump))

    def reload(self):
        """
        Reloads objects from the JSON file into the storage.
        """
        from models.base_model import BaseModel
        cls_dicts = {
            "BaseModel": BaseModel
        }
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.loads(f.read())
            for key, value in data.items():
                self.__objects[key] = cls_dicts[value['__class__']](**value)
        except FileNotFoundError:
            pass
