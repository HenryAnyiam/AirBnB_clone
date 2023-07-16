#!/usr/bin/python3
""" user test cases """


import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):

    def test_user_attr(self):
        user = User()
        self.assertEqual('', user.first_name)
        self.assertEqual('', user.last_name)
        self.assertEqual('', user.email)
        self.assertEqual('', user.password)

    def test_user_attr_update(self):
        user = User()
        user.first_name = 'Muhluri'
        user.last_name = 'Test'
        user.email = 'test@gmail.com'
        user.password = 'test'
        self.assertEqual(user.first_name, 'Muhluri')
        self.assertEqual(user.last_name, 'Test')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertEqual(user.password, 'test')

    def test_user_to_dict(self):
        user = User()
        user.first_name = 'Muhluri'
        user.last_name = 'Test'
        user.email = 'test@gmail.com'
        user.password = 'test'
        user_dict = user.to_dict()
        self.assertEqual(user_dict['first_name'], 'Muhluri')
        self.assertEqual(user_dict['last_name'], 'Test')
        self.assertEqual(user_dict['email'], 'test@gmail.com')
        self.assertEqual(user_dict['password'], 'test')

    def test_user_from_dict(self):
        user_dict = {
            'id': '123',
            'created_at': '2023-07-15T13:08:00',
            'updated_at': '2023-07-15T13:08:00',
            'email': 'test@gmail.com',
            'password': 'password321',
            'first_name': 'test',
            'last_name': 'just'
                }
        user = User(**user_dict)
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'just')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertEqual(user.password, 'password321')

    def test_user_save(self):
        user = User()
        user.first_name = 'Test'
        user.last_name = 'Just'
        user.save()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        user_key = 'User.' + user.id
        self.assertIn(user_key, storage.all())


if __name__ == '__main__':
    unittest.main()
