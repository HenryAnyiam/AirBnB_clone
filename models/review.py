#!/usr/bin/python3

"""module containing class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """building class Review that inherits
    from class BaseModel"""

    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """initialization of class Review"""

        BaseModel.__init__(self, *args, **kwargs)
