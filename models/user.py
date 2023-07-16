#!/usr/bin/python3

"""module containing class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """building class User that inherits
    from class BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """initialization of class User"""

        BaseModel.__init__(self, *args, **kwargs)
