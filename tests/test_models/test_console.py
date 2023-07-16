#!/usr/bin/python3
""" console test cases """


import unittest
from io import StringIO
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel


class HBNBCommandTesCase(unittest.TestCase):
    """ console unittests """
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            output = f"BaseModel.{output}"
            self.assertTrue(output)
            self.assertIn(output, storage.all())
            self.assertIsInstance(storage.all()[output], BaseModel)

    def test_create_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_non_exist(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        model = BaseModel()
        storage.new(model)
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'show BaseModel {model.id}')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(model))

    def test_show_non_existent_class(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('show BaseName')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_no_class(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('show')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_no_id(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('show BaseModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_non_existance(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('show BaseModel 121212')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy(self):
        obj = BaseModel()
        storage.new(obj)
        obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy BaseModel {}'.format(obj.id))
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(obj.id, storage.all())

    def test_destroy_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy BaseModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destrooy_non_existent_className(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy BaseModel 121212')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        obj1.save()
        obj2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('all BaseModel')
            output = fake_out.getvalue().strip()
            self.assertIn(str(obj1), output)
            self.assertIn(str(obj2), output)

    def test_all_class_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('all MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        obj = BaseModel()
        storage.new(obj)
        obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel {} email "airbnb.gmail.com"'
                                .format(obj.id))
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(obj.email, "airbnb.gmail.com")
            self.assertTrue(hasattr(obj, 'updated_at'))

    def test_update_non_existent(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_non_existent_class(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel 121212')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_missing_attr(self):
        obj = BaseModel()
        storage.new(obj)
        obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel {}'.format(obj.id))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_missing_value(self):
        obj = BaseModel()
        storage.new(obj)
        obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel {} email'.format(obj.id))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** value missing **')


if __name__ == '__main__':
    unittest.main()
