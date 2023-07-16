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
    def test_state_inherits_base_model(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_has_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

    def test_state_has_correct_class_name(self):
        state = State()
        self.assertEqual(state.__class__.__name__, 'State')


class TestCity(unittest.TestCase):
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


class TestAmenity(unittest.TestCase):
    def test_amenity_inherits_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_has_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

    def test_amenity_has_correct_class_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, 'Amenity')


class TestPlace(unittest.TestCase):
    def test_place_inherits_base_model(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_has_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_has_correct_class_name(self):
        place = Place()
        self.assertEqual(place.__class__.__name__, 'Place')


class TestReview(unittest.TestCase):
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
