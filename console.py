#!/usr/bin/python3

"""module for the HBNBCommand"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The Console - command interpreter"""

    prompt = "(hbnb) "
    __class = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """handle EOF command"""

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """overwrites Base Class method
        executes nothing when line is empty"""

        pass

    def do_create(self, line):
        """creates a new object instance, saves it
        and prints the ID"""

        if len(line) == 0:
            print("** class name missing **")
        else:
            if line not in self.__class:
                print("** class doesn't exist **")
            else:
                obj = eval(line)
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
            if args[0] not in self.__class:
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

    def do_destroy(self, line):
        """ destroys an instance based on the class name and id
        save the changes into the JSON file"""

        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in self.__class:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = ".".join(args)
                objs = storage.all()
                if key in objs.keys():
                    del objs[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """ prints all string representation
        of all instances in a list format"""

        objs = storage.all()
        if len(line) == 0:
            output = [str(i) for i in objs.values()]
            print(output)
        else:
            if line in self.__class:
                output = []
                for key, value in objs.items():
                    if line in key:
                        output.append(str(value))
                print(output)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """updates/adds an instance attribute based on the
        class nane and ID and saves the changes"""

        args = line.split()
        errors = ["** class name missing **", "** instance id missing **",
                  "** attribute name missing **", "** value missing **"]
        objs = storage.all()
        if (len(args) > 0) and (args[0] not in self.__class):
            print("** class doesn't exist **")
        elif (len(args) > 1) and (".".join(args[:2]) not in objs.keys()):
            print("** no instance found **")
        elif len(args) < 4:
            for i in range(3):
                if len(args) == i:
                    print(errors[i])
        else:
            key = ".".join(args[:2])
            instance = objs[key]
            i_type = type(args[3])
            hold = instance.to_dict()
            if args[2] in hold.keys():
                i_type = type(hold[args[2]])
            if args[3][0] == '"' and args[3][-1] != '"':
                i = 4
                while (len(args) > i):
                    args[3] += " " + args[i]
                    if args[i][-1] == '"':
                        break
            if args[3][0] == '"':
                args[3] = args[3][1:-1]
            setattr(instance, args[2], i_type(args[3]))
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
