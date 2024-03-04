#!/usr/bin/python3
"""Unittest for base model module
"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_model = BaseModel()

    def test_BaseModel_instance_is_init(self):
        self.assertTrue(isinstance(self.test_model, BaseModel))

    def test_BaseModel_has_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModel_has_methods(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_BaseModel_init_method(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, type(datetime.now()))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, type(datetime.now()))

    def test_BaseModel_str_method(self):
        obj = BaseModel()
        obj_str = "[{}] ({}) {}".format(
            obj.__class__.__name__, obj.id,
            self.__dict__)
        self.assertTrue(str(obj), obj_str)

    def test_BaseModel_save_method(self):
        self.test_model.save()
        self.assertNotEqual(
            self.test_model.created_at.isoformat(),
            self.test_model.updated_at.isoformat())

    def test_BaseModel_to_dict_method(self):
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


if __name__ == "__main__":
    unittest.main()
