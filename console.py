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

    def default(self, line):
        """overwrites base class default
        handles commands not found"""

        if ("." and "(" and ")") in line:
            c_start = line.index(".")
            c_end = line.index("(")
            end = len(line) - 1
            if c_start < c_end and line[end] == ")":
                comm = line[(c_start + 1):c_end]
                comms = {"all": self.do_all,
                         "count": self.do_count,
                         "show": self.do_show,
                         "update": self.do_update}
                command = [line[0:c_start]]
                if (end - c_end) > 1:
                    hold = line[c_end + 1:end].split(", ")
                    command += hold
                command = " ".join(command)
                for key in comms.keys():
                    if comm == key:
                        comms[key](command)
                if comm not in comms.keys():
                    cmd.Cmd.default(self, line)
            else:
                cmd.Cmd.default(self, line)
        else:
            cmd.Cmd.default(self, line)

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
                args[1] = args[1].strip('"')
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
                args[1] = args[1].strip('"')
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

    def do_count(self, line):
        """prints number of instances of
        a particular class"""

        if len(line) == 0:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in self.__class:
                print("** class doesn't exist **")
            else:
                objs = storage.all()
                i_num = 0
                for key in objs.keys():
                    if line in key:
                        i_num += 1
                print(i_num)

    def do_update(self, line):
        """updates/adds an instance attribute based on the
        class nane and ID and saves the changes"""

        args = line.split()
        errors = ["** class name missing **", "** instance id missing **",
                  "** attribute name missing **", "** value missing **"]
        objs = storage.all()
        if len(args) >= 2:
            args[1] = args[1].strip('"')
            args[2] = args[2].strip('"')
        if (len(args) > 0) and (args[0] not in self.__class):
            print("** class doesn't exist **")
        elif (len(args) > 1) and (".".join(args[:2]) not in objs.keys()):
            print("** no instance found **")
        elif len(args) < 4:
            for i in range(4):
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
