#!/usr/bin/python3

"""module containing class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """building class City that inherits
    from class BaseModel"""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """initialization of class City"""

        BaseModel.__init__(self, *args, **kwargs)
