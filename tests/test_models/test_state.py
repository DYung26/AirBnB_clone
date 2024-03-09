#!/usr/bin/python3
"""
Module: test_state.py
This module defines Tests for the State model
"""
import unittest
import time
from models.state import State


class TestState(unittest.TestCase):
    """TestState Tests State model class

    Args:
        unittest (class): TestCase unittest parent class
    """
    def setUp(self):
        self.state = State()

    def test_attributes_default_values(self):
        """Test atrribute default values"""
        self.assertEqual(self.state.name, "")

    def test_attributes_types(self):
        """Tests attributes types"""
        self.assertIsInstance(self.state.name, str)

    def test_inherited_attributes(self):
        """Tests initialization of inherited attributes"""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_str_representation(self):
        """Tests the __str__ method"""
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_save_method(self):
        """Tests the save method of the class"""
        original_updated_at = self.state.updated_at
        time.sleep(0.1)
        self.state.save()
        self.assertNotEqual(original_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of the class"""
        expected_dict = {
            '__class__': "State",
            'name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.state.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.state, key))


if __name__ == '__main__':
    unittest.main()
