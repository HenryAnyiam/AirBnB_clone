#!/usr/bin/python3
""" testing all classes """


import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestState(unittest.TestCase):
    """ tests if state is subclass of base model"""

    def test_state_inherits_base_model(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_has_attributes(self):
        """ teset all the state attributes """

        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

    def test_state_has_correct_class_name(self):
        """ Test if theres a correct class name"""
        state = State()
        self.assertEqual(state.__class__.__name__, 'State')
