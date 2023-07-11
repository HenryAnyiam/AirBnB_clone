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
