#!/usr/bin/python3
""" console test cases """


import unittest
from io import StringIO
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel

class HBNBCommandTesCase(unittest.TestCase):
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
            self.console.onecmd(f'show BaseModel {model.id}' )
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

if __name__ == '__main__':
    unittest.main()
