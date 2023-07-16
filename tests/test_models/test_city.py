#!/usr/bin/python3
""" testing all classes """


import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestCity(unittest.TestCase):
    """test to make sure city is sublclass of base model """
    def test_city_inherits_base_model(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_has_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_city_has_correct_class_name(self):
        city = City()
        self.assertEqual(city.__class__.__name__, 'City')


if __name__ == '__main__':
    unittest.main()
