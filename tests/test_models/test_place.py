#!/usr/bin/python3
"""
    Unit tests for Place
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
import pycodestyle


class PlaceTest(unittest.TestCase):
    """Test for Place"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/place.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

    def test_subclass(self):
        """test if Place is subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_instance(self):
        """test instance of class"""
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])
        self.assertTrue(isinstance(my_place, BaseModel))


if __name__ == '__main__':
    unittest.main()
