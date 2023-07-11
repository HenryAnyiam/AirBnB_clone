#!/usr/bin/python3
"""
    unittests for the user id
"""


import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test class for the id attribute ensuring that the id are unique and
        correctly formatted."""

    def test_uuid(self):
        """ tests cases to the the id of the BaseModel class """

        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsNotNone(bm1.id)
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_create_at_updated_at(self):
        """ test cases for created_at """

        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime.datetime)
        self.assertIsInstance(bm1.updated_at, datetime.datetime)

    def test_kwargs_init(self):
        """ test base model with kwargs initialisation """

        date_tomorrow = '2023-08-11T21:12:23'
        date_iso = datetime.datetime.fromisoformat(date_tomorrow)
        bm1 = BaseModel(id='123', created_at=date_tomorrow,
                        random_arg='test')
        self.assertEqual(bm1.id, '123')
        self.assertEqual(bm1.created_at, date_iso)
        self.assertEqual(bm1.random_arg, 'test')

    def test_str(self):

        bm1 = BaseModel(id='123', rnd_arg='test')
        expctd_prnt = "[BaseModel] (123) {'id': '123',\
                        'created_at': datetime.datetime(...)\
                        'updated_at': datetime.datetime(...)\
                        'rnd_arg': 'test'}"
        self.assertEqual(str(bm1), expct_prnt)

    def test_save(self):

        bm1 = BaseModel()
        time.sleep(10)
        bm1.save()
        self.assertIsNotEqual(bm1.created_at.isoformat(),
                            bm1.updated_at.isoformat())

