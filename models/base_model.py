#!/usr/bin/python3

"""module with creation of BaseModel classdefines common attributes/methods for
 every other class in the AirBnB console"""

import json
import uuid
import datetime


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
                elif key == "created_at" or key == "updated_at":
                    temp = datetime.datetime.fromisoformat(value)
                    setattr(self, key, temp)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
