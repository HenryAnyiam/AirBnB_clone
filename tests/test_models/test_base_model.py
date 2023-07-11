#!/usr/bin/python3
"""
    unittests for the user id
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for the id attribute ensuring that the id are unique and
        correctly formatted."""

    def test_uuid(self):
        """ tests cases to the the id of the BaseModel class """

        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
