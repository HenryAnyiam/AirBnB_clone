#!/usr/bin/python3
""" file storafe test cases """


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os


class FileStorageTestCase(unittest.TestCase):
    """ test cases for file storage """

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        model = BaseModel()
        self.storage.new(model)
        objects = self.storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, objects)

    def test_save(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, objects)



if __name__ == "__main__":
    unittest.main()
