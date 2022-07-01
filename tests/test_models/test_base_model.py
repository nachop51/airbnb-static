#!/usr/bin/python3
"""
    Unit tests for BaseModel
"""

import unittest
from models.base_model import BaseModel
import pycodestyle
from datetime import datetime

class BaseModelTest(unittest.TestCase):
    """Test for BaseModel"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

    def test_attr(self):
        """test class attributes"""
        my_baseModel = BaseModel()
        self.assertIs(type(my_baseModel.id), str)
        self.assertIs(type(my_baseModel.created_at), datetime)
        self.assertIs(type(my_baseModel.updated_at), datetime)

    def test_str(self):
        """test __str__ method"""
        my_baseModel = BaseModel()
        self.assertEqual(f"[{type(my_baseModel).__name__}] ({my_baseModel.id}) {my_baseModel.__dict__}", str(my_baseModel))

if __name__ == '__main__':
    unittest.main()
