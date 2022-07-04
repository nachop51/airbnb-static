#!/usr/bin/python3
"""
    Unittest for FileStorage
"""

import unittest
import pycodestyle
import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import pathlib as pl


class FileStorageTest(unittest.TestCase):
    """Test for file_storage.py"""

    def test_pep8(self):
        """Check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            check.total_errors, 0, "Found style errors"
        )
    
    def test_classes(self):
        """check the class is created"""
        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                models.engine.file_storage.FileStorage)
    
    def test_attr(self):
        """test are attributes"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_models(self):
        """check if all is working"""
        self.assertIsNotNone(models.storage.all())

    def test_reload_method(self):
        """check if reload working"""
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)
    
    @classmethod
    def setUpClass(self):
        """set instance"""
        self.myModel = BaseModel()
        self.storage = FileStorage()

    def test_doc_module(self):
        """test doc module"""
        self.assertGreater(len(FileStorage.__doc__), 1)

    def test_doc_string(self):
        """test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_doc_class(self):
        """test doc class"""
        self.assertGreater(len(FileStorage.__doc__), 1)

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

    def test_reload(self):
        """test reload method"""
        self.myModel.name = "MyModelTest"
        self.myModel.number = 183
        name = str(self.myModel.__class__.__name__)
        key = name + "." + str(self.myModel.id)
        self.myModel.save()
        self.storage.reload()
        objs = self.storage.all()
        self.obj_reload = objs[key]
        self.assertTrue(self.myModel.__dict__ == self.obj_reload.__dict__)
        self.assertTrue(self.myModel is not self.obj_reload)
        self.assertIsInstance(self.obj_reload, BaseModel)
        self.assertTrue(self.storage.all(), "MyModelTest")


if __name__ == "__main__":
    unittest.main()
