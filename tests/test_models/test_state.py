#!/usr/bin/python3
"""
    Unit tests for State
"""

import unittest
from models.base_model import BaseModel
from models.state import State
import pycodestyle

class StateTest(unittest.TestCase):
    """Test for State"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/state.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

    def test_subclass(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
    
    def test_attr(self):
        """test atributte class"""
        self.assertEqual(State.name, "")

if __name__ == '__main__':
    unittest.main()
