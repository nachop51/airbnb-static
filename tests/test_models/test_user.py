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

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_instance(self):
        """test instance class"""
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")
        self.assertTrue(isinstance(my_user, BaseModel))


if __name__ == '__main__':
    unittest.main()
