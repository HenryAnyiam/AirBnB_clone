#!/usr/bin/python3

"""module containing class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """building class Place that inherits
    from class BaseModel"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
    price_by_night = 0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initialization of class Place"""

        BaseModel.__init__(self, *args, **kwargs)
