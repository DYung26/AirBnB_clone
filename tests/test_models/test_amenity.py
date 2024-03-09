#!/usr/bin/python3
"""
Test module for Amenity class

This module contains a series of unit tests to
validate the behavior of the Amenity class.

Attributes:
    TestAmenity (unittest.TestCase): The test case class for Amenity.
"""

import unittest
import time
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test case class for Amenity

    Attributes:
        amenity (Amenity): An instance of the Amenity class for testing.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.

        Creates an instance of the Amenity class for testing.
        """
        self.amenity = Amenity()

    def test_attributes_default_values(self):
        """Test default values of attributes in Amenity instance"""
        self.assertEqual(self.amenity.name, "")

    def test_attributes_types(self):
        """Test types of attributes in Amenity instance"""
        self.assertIsInstance(self.amenity.name, str)

    def test_inherited_attributes(self):
        """Test inherited attributes in Amenity instance"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_str_representation(self):
        """Test string representation of Amenity instance"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_method(self):
        """Test save method of Amenity instance"""
        original_updated_at = self.amenity.updated_at
        time.sleep(0.1)
        self.amenity.save()
        self.assertNotEqual(original_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of Amenity instance"""
        expected_dict = {
            '__class__': "Amenity",
            'name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.amenity.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.amenity, key))


if __name__ == '__main__':
    unittest.main()
