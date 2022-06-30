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

if __name__ == '__main__':
    unittest.main()
