#!/usr/bin/python3

"""module with FileStorage class"""


import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
        deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns ductionary with object instances"""

        return self.__objects

    def new(self, obj):
        """adds new instance to dictionary storage

        Args:
            obj: instance to save

        """

        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes and saves __objects"""

        with open(self.__file_path, "w", encoding="UTF-8") as MyFile:
            hold = {}
            for key, item in self.__objects.items():
                hold[key] = item.to_dict()
            json.dump(hold, MyFile)

    def reload(self):
        """deserializes and loads __objects"""

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as MyFile:
                hold = json.load(MyFile)
                for i in hold.keys():
                    name = hold[i]["__class__"]
                    obj = eval(name)(**hold[i])
                    self.new(obj)
        except FileNotFoundError:
            pass
