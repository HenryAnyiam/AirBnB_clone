#!/usr/bin/python3
""" testing all classes """


import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestAmenity(unittest.TestCase):
    """ tests that amenity is a subclass of Basemodel """
    def test_amenity_inherits_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_has_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

    def test_amenity_has_correct_class_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, 'Amenity')
