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

    def test_instance(self):
        """test instance of class"""
        my_state = State()
        self.assertEqual(my_state.name, "")
        self.assertTrue(isinstance(my_state, BaseModel))


if __name__ == '__main__':
    unittest.main()
