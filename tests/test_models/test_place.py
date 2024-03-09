#!/usr/bin/python3
"""
Module: test_place.py
This module defines Tests for the Place model
"""
import unittest
import time
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace Tests Place model class

    Args:
        unittest (class): TestCase unittest parent class
    """
    def setUp(self):
        self.place = Place()

    def test_attributes_default_values(self):
        """Test atrribute default values"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attributes_types(self):
        """Tests attributes types"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_inherited_attributes(self):
        """Tests initialization of inherited attributes"""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_str_representation(self):
        """Tests the __str__ method"""
        expected_str = "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_save_method(self):
        """Tests the save method of the class"""
        original_updated_at = self.place.updated_at
        time.sleep(0.1)
        self.place.save()
        self.assertNotEqual(original_updated_at, self.place.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of the class"""
        expected_dict = {
            'id': self.place.id,
            '__class__': "Place",
            'created_at': self.place.created_at,
            'updated_at': self.place.updated_at,
            'city_id': "",
            'user_id': "",
            'name': "",
            'description': "",
            'number_rooms': 0,
            'number_bathrooms': 0,
            'max_guest': 0,
            'price_by_night': 0,
            'latitude': 0.0,
            'longitude': 0.0,
            'amenity_ids': []
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.place.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.place, key))


if __name__ == '__main__':
    unittest.main()
