#!/usr/bin/python3
"""
Test module for City class

This module contains a series of unit tests to validate
the behavior of the City class.

Attributes:
    TestCity (unittest.TestCase): The test case class for City.
"""

import unittest
import time
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test case class for City

    Attributes:
        city (City): An instance of the City class for testing.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.

        Creates an instance of the City class for testing.
        """
        self.city = City()

    def test_attributes_default_values(self):
        """Test default values of attributes in City instance"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attributes_types(self):
        """Test types of attributes in City instance"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inherited_attributes(self):
        """Test inherited attributes in City instance"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_str_representation(self):
        """Test string representation of City instance"""
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save_method(self):
        """Test save method of City instance"""
        original_updated_at = self.city.updated_at
        time.sleep(0.1)
        self.city.save()
        self.assertNotEqual(original_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of City instance"""
        expected_dict = {
            '__class__': "City",
            'state_id': "",
            'name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.city.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.city, key))


if __name__ == '__main__':
    unittest.main()
