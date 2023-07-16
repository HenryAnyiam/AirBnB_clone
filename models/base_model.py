#!/usr/bin/python3
"""
AirBnB Console - BaseModel Module

This module contains the definition of the BaseModel class,
which serves as the base class for other classes in the AirBnB console.

Attributes:
    None

Methods:
    BaseModel.__init__(*args, **kwargs):
        Initialization method for BaseModel instances.

    BaseModel.__str__():
        Returns a string representation of a BaseModel instance.

    BaseModel.save():
        Updates the updated_at attribute and saves the instance.

    BaseModel.to_dict():
        Returns a dictionary representation of a BaseModel instance.
"""


import json
import uuid
import datetime
import models


class BaseModel:
    """defines common attributes/methods for
    every other class in the AirBnB console"""

    def __init__(self, *args, **kwargs):
        """initialization of BaseModel

        Args:
            args: unused parameter
            kwargs: dictionary containing attribute details

        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key in ("created_at", "updated_at"):
                    temp = datetime.datetime.fromisoformat(value)
                    setattr(self, key, temp)
                else:
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs.keys():
                self.created_at = datetime.datetime.today()
            if "updated_at" not in kwargs.keys():
                self.updated_at = datetime.datetime.today()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self):
        """print string representation of class instance"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with current time after changes"""

        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a serialized objext of class instance"""

        hold = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                hold[key] = value.isoformat()
            else:
                hold[key] = value
        hold["__class__"] = type(self).__name__
        return hold
