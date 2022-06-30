#!/usr/bin/python3
"""
    Unit tests for User
"""

import unittest
from models.base_model import BaseModel
from models.user import User
import pycodestyle

class UserTest(unittest.TestCase):
    """Test for User"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

if __name__ == '__main__':
    unittest.main()
