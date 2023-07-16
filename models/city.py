#!/usr/bin/python3

"""module containing class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """building class City that inherits
    from class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialization of class City"""
        """ self.name = ""
        self.state_id = "" """

        BaseModel.__init__(self, *args, **kwargs)
