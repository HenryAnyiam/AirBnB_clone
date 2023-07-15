#!/usr/bin/python3

"""module containing class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """building class Place that inherits
    from class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialization of class Place"""
        self.name = ""
        self.city_id = ""
        self.user_id = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by__night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.price_by_night = 0
        self.amenity_ids = []

        BaseModel.__init__(self, *args, **kwargs)
