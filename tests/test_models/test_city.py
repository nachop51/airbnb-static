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

if __name__ == '__main__':
    unittest.main()
