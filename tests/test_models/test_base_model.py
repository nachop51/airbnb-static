#!/usr/bin/python3
"""
    Unit tests for BaseModel
"""

import unittest
from models.base_model import BaseModel
import pycodestyle
from datetime import datetime
from models.engine.file_storage import FileStorage
from os import path


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
        m = BaseModel()
        self.assertEqual(f"[{type(m).__name__}] ({m.id}) {m.__dict__}", str(m))

    def test_save(self):
        """test save method"""
        my_baseModel = BaseModel()
        my_fileStorage = FileStorage()
        update = my_baseModel.__dict__['updated_at']
        my_baseModel.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(my_baseModel.__dict__['updated_at'], update)
        update = my_baseModel.__dict__['updated_at']
        my_fileStorage.reload()
        self.assertEqual(my_baseModel.__dict__['updated_at'], update)

    def test_to_dict(self):
        """test to_dict_method"""
        bm = BaseModel()
        self.assertEqual(bm.to_dict()["id"], bm.id)
        self.assertEqual(bm.to_dict()["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm.to_dict()["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm.to_dict()['__class__'], bm.__class__.__name__)

    def test_not_equal_id(self):
        """test two instane ids"""
        id_a = BaseModel()
        id_b = BaseModel()
        self.assertNotEqual(id_a.id, id_b.id)


if __name__ == '__main__':
    unittest.main()
