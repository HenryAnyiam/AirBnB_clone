#!/usr/bin/python3

"""module containing class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """building class User that inherits
    from class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialization of class User"""
        """self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = "" """

        BaseModel.__init__(self, *args, **kwargs)
