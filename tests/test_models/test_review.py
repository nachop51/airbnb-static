#!/usr/bin/python3
"""
    Unit tests for Review
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
import pycodestyle

class ReviewTest(unittest.TestCase):
    """Test for Review"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

if __name__ == '__main__':
    unittest.main()
