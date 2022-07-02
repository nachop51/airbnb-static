#!/usr/bin/python3
"""
    Unit tests for Amenity
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pycodestyle


class AmenityTest(unittest.TestCase):
    """Test for Amenity"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/amenity.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

    def test_subclass(self):
        """test if Amenity is subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(Amenity.name, "")

    def test_instance(self):
        """Test instance of class"""
        my_amenity = Amenity()
        self.assertEqual(my_amenity.name, "")
        self.assertTrue(isinstance(my_amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
