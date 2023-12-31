#!/usr/bin/python3

"""module containing class State"""

from models.base_model import BaseModel


class State(BaseModel):
    """building class State that inherits
    from class BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initialization of class State"""

        BaseModel.__init__(self, *args, **kwargs)
