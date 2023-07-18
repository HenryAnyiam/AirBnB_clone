#!/usr/bin/python3
""" console test cases """


import os
import unittest
from io import StringIO
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommandTesCase(unittest.TestCase):
    """ console unittests """
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_quit(self):
        self.assertTrue(self.console.onecmd('quit'))

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
        Smodel = State()
        Cmodel = City()
        Pmodel = Place()
        Rmodel = Review()
        Amodel = Amenity()
        Umodel = User()
        storage.new(Smodel)
        storage.new(Cmodel)
        storage.new(Pmodel)
        storage.new(Rmodel)
        storage.new(Amodel)
        storage.new(Umodel)
        Smodel.save()
        Pmodel.save()
        Cmodel.save()
        Rmodel.save()
        Amodel.save()
        Umodel.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'show BaseModel {model.id}')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(model))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'BaseModel.show("{model.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(model))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'User.show("{Umodel.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(Umodel))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'State.show("{Smodel.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(Smodel))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'City.show("{Cmodel.id})')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(Cmodel))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'Amenity.show("{Amodel.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(Amodel))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'Place.show("{Pmodel.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(Pmodel))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'Review.show("{Rmodel.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(Rmodel))

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
        B_obj = BaseModel()
        U_obj = User()
        S_obj = State()
        C_obj = City()
        A_obj = Amenity()
        R_obj = Review()
        P_obj = Place()
        storage.new(obj)
        storage.new(U_obj)
        storage.new(S_obj)
        storage.new(C_obj)
        storage.new(A_obj)
        storage.new(R_obj)
        storage.new(P_obj)
        storage.new(B_obj)
        obj.save()
        B_obj.save()
        U_obj.save()
        S_obj.save()
        C_obj.save()
        A_obj.save()
        P_obj.save()
        R_obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('destroy BaseModel {}'.format(obj.id))
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'BaseModel.destroy("{B_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(B_obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'User.destroy("{U_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(U_obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'State.destroy("{S_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(S_obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'City.destroy("{C_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(C_obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'Place.destroy("{P_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(C_obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'Review.destroy("{R_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(C_obj.id, storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'Amenity.destroy("{A_obj.id}")')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertNotIn(A_obj.id, storage.all())

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
        U_obj = User()
        S_obj = State()
        C_obj = City()
        A_obj = Amenity()
        P_obj = Place()
        R_obj = Review()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(U_obj)
        storage.new(S_obj)
        storage.new(C_obj)
        storage.new(A_obj)
        storage.new(P_obj)
        storage.new(R_obj)
        obj1.save()
        obj2.save()
        U_obj.save()
        S_obj.save()
        C_obj.save()
        A_obj.save()
        P_obj.save()
        R_obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('all BaseModel')
            output = fake_out.getvalue().strip()
            self.assertIn(str(obj1), output)
            self.assertIn(str(obj2), output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('BaseModel.all()')
            output = fake_out.getvalue().strip()
            self.assertIn(str(obj1), output)
            self.assertIn(str(obj2), output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('User.all()')
            output = fake_out.getvalue().strip()
            self.assertIn(str(U_obj), output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('State.all()')
            output = fake_out.getvalue().strip()
            self.assertIn(str(S_obj), output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('Amenity.all()')
            output = fake_out.getvalue().strip()
            self.assertIn(str(A_obj), output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('Place.all()')
            output = fake_out.getvalue().strip()
            self.assertIn(str(P_obj), output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('Review.all()')
            output = fake_out.getvalue().strip()
            self.assertIn(str(R_obj), output)

    def test_all_class_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('all MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        Bobj = BaseModel()
        storage.new(Bobj)
        Bobj.save()
        Sobj = State()
        Cobj = City()
        Pobj = Place()
        Robj = Review()
        Aobj = Amenity()
        Uobj = User()
        storage.new(Sobj)
        storage.new(Cobj)
        storage.new(Pobj)
        storage.new(Robj)
        storage.new(Aobj)
        storage.new(Uobj)
        Sobj.save()
        Cobj.save()
        Pobj.save()
        Robj.save()
        Aobj.save()
        Uobj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('BaseModel.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('User.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('State.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('City.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('Place.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('Amenity.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('Review.count()')
            output = fake_out.getvalue().strip()
            self.assertEqual('1', output)

    def test_update(self):
        obj = BaseModel()
        storage.new(obj)
        obj.save()
        Sobj = State()
        Cobj = City()
        Pobj = Place()
        Robj = Review()
        Aobj = Amenity()
        Uobj = User()
        storage.new(Sobj)
        storage.new(Cobj)
        storage.new(Pobj)
        storage.new(Robj)
        storage.new(Aobj)
        storage.new(Uobj)
        Sobj.save()
        Cobj.save()
        Pobj.save()
        Robj.save()
        Aobj.save()
        Uobj.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('update BaseModel {} email "airbnb.gmail.com"'
                                .format(obj.id))
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(obj.email, "airbnb.gmail.com")
            self.assertTrue(hasattr(obj, 'updated_at'))
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'BaseModel.update("{obj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(obj.email, "hbnb.gmail.com")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'User.update("{Uobj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(Uobj.email, "hbnb.gmail.com")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'State.update("{Sobj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(Sobj.email, "hbnb.gmail.com")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'City.update("{Cobj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(Cobj.email, "hbnb.gmail.com")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'Review.update("{Robj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(Robj.email, "hbnb.gmail.com")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'Place.update("{Pobj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(Pobj.email, "hbnb.gmail.com")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            cmnd = f'Amenity.update("{Aobj.id}" "email" "hbnb.gmail.com")'
            self.console.onecmd(cmnd)
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)
            self.assertEqual(Aobj.email, "hbnb.gmail.com")

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

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('')
            output = fake_out.getvalue().strip()
            self.assertEqual('', output)


if __name__ == '__main__':
    unittest.main()
