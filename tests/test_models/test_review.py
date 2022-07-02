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

    def test_subclass(self):
        """test if Review is subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attr(self):
        """test attributes class"""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_instance(self):
        """test instance class"""
        my_review = Review()
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")


if __name__ == '__main__':
    unittest.main()
