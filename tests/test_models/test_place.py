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

if __name__ == '__main__':
    unittest.main()
