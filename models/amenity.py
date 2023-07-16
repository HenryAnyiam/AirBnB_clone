#!/usr/bin/python3

"""module containing class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """building class Amenity that inherits
    from class BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of class Amenity"""

        BaseModel.__init__(self, *args, **kwargs)
