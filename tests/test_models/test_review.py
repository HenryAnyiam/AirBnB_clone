#!/usr/bin/python3
""" testing all classes """


import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestReview(unittest.TestCase):
    """ test review attributes and that review is subclass of BaseModel """
    def test_review_inherits_base_model(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_has_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_review_has_correct_class_name(self):
        review = Review()
        self.assertEqual(review.__class__.__name__, 'Review')


if __name__ == '__main__':
    unittest.main()
