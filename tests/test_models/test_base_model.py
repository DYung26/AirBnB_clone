#!/usr/bin/python3
"""Unittest for base model module

This module contains unit tests for the BaseModel class and its methods.
"""

from datetime import datetime
import unittest
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class

    This class contains unit tests for the BaseModel class and its methods.
    """

    def setUp(self):
        """setUp method

        This method sets up the test environment before each test case.
        It creates a new instance of the BaseModel class for testing.
        """
        self.test_model = BaseModel()

    def test_basemodel_instance_is_init(self):
        """Test that BaseModel instance is initialized properly

        This test verifies that the BaseModel instance is initialized
        properly and is an instance of the BaseModel class.
        """
        self.assertTrue(isinstance(self.test_model, BaseModel))

    def test_basemodel_has_docstrings(self):
        """Test that BaseModel and its methods have docstrings

        This test verifies that the BaseModel class and its methods have
        docstrings defined.
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_basemodel_has_methods(self):
        """Test that BaseModel has required methods

        This test verifies that the BaseModel class has the required methods
        defined.
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_basemodel_init_method(self):
        """Test BaseModel __init__ method

        This test verifies that the __init__ method of the BaseModel class
        initializes instance attributes properly.
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, type(datetime.now()))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, type(datetime.now()))

    def test_basemodel_str_method(self):
        """Test BaseModel __str__ method

        This test verifies that the __str__ method of the BaseModel class
        returns a user-friendly string representation of the object.
        """
        obj = BaseModel()
        obj_str = "[{}] ({}) {}".format(
            obj.__class__.__name__, obj.id,
            self.__dict__)
        self.assertTrue(str(obj), obj_str)

    def test_basemodel_save_method(self):
        """Test BaseModel save method

        This test verifies that the save method of the BaseModel class
        updates the updated_at attribute with the current datetime.
        """
        time.sleep(1)
        self.test_model.save()
        self.assertNotEqual(
            self.test_model.created_at.isoformat(),
            self.test_model.updated_at.isoformat())

    def test_basemodel_to_dict_method(self):
        """Test BaseModel to_dict method

        This test verifies that the to_dict method of the BaseModel class
        returns a dictionary representation of the object's attributes.
        """
        obj = self.test_model.to_dict()
        self.assertEqual(
            obj['__class__'],
            self.test_model.__class__.__name__)
        self.assertIsInstance(obj['created_at'], str)
        self.assertIsInstance(obj['updated_at'], str)
        obj = BaseModel()
        new_dict = obj.__dict__.copy()
        new_dict["__class__"] = obj.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        self.assertDictEqual(new_dict, obj.to_dict())

    def test_json_to_basemodel(self):
        """Test JSON to BaseModel conversion

        This test verifies that a dictionary representing a BaseModel object
        can be successfully converted back to a BaseModel instance.
        """
        date = datetime.now()
        date_to_string = date.isoformat()
        _dict = {
            "id": "d31f77d7-f6a3-484c-a66a-32453dbcab66",
            "created_at": date_to_string,
            "updated_at": date_to_string,
            "__class__": "TestModel",
            "additional_attr": "Dummy Value"}
        test_cls = BaseModel(**_dict)
        self.assertEqual(test_cls.__class__.__name__, "BaseModel")
        self.assertNotIn('__class__', test_cls.__dict__)
        self.assertEqual(test_cls.id, "d31f77d7-f6a3-484c-a66a-32453dbcab66")
        self.assertEqual(type(test_cls.created_at), type(date))
        self.assertEqual(type(test_cls.updated_at), type(date))
        self.assertEqual(test_cls.__dict__['additional_attr'], "Dummy Value")


if __name__ == "__main__":
    unittest.main()
