#!/usr/bin/python3
"""
    Unit tests for City
"""

import unittest
from models.base_model import BaseModel
from models.city import City
import pycodestyle


class CityTest(unittest.TestCase):
    """Test for City"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/city.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

    def test_subclass(self):
        """test if City is subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_atrr(self):
        """test atributtes class"""
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_instance(self):
        """Test instance class"""
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")


if __name__ == '__main__':
    unittest.main()
