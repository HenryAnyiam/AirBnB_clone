#!/usr/bin/python3

"""module for the HBNBCommand"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The Console - command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """handle EOF command"""

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """creates a new object instance, saves it
        and prints the ID"""

        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                obj = eval(line)
            except NameError:
                print("** class doesn't exist **")
            else:
                if not isinstance(obj, type):
                    print("** class doesn't exist **")
                else:
                    new_obj = obj()
                    new_obj.save()
                    print(new_obj.id)

    def do_show(self, line):
        """prints the string representation of an
        instance based on the class name and id"""

        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split()
            try:
                obj = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
            else:
                if not isinstance(obj, type):
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = ".".join(args)
                    objs = storage.all()
                    if key in objs.keys():
                        print(objs[key])
                    else:
                        print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
