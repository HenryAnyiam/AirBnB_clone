#!/usr/bin/python3

"""module containing class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """building class Review that inherits
    from class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialization of class Review"""
        self.text = ""
        self.place_id = ""
        self.user_id = ""

        BaseModel.__init__(self, *args, **kwargs)
