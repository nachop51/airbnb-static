#!/usr/bin/python3
"""
    Unittest for FileStorage
"""
import unittest
import pycodestyle
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    """Test for file_storage.py"""

    def test_pep8(self):
        """Check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            check.total_errors, 0, "Found style errors"
        )

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all(self):
        """Test all method"""
        fileStorage = FileStorage()
        storageAll = fileStorage.all()
        self.assertIsNotNone(storageAll)
        self.assertIs(storageAll, fileStorage._FileStorage__objects)
        self.assertEqual(storageAll, fileStorage._FileStorage__objects)

    def test_new(self):
        """test new method"""
        fileStorage = FileStorage()
        storageAll = fileStorage.all()
        pool = Amenity()
        pool.id = "AAAA0"
        pool.name = "Heated Pool"
        fileStorage.new(pool)
        key = pool.__class__.__name__ + "." + pool.id
        self.assertIsNotNone(storageAll[key])


if __name__ == "__main__":
    unittest.main()
