#!/usr/bin/python3
"""The Review Class Definition"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews the user/place/text as part of the ID
    """

    place_id = ""
    user_id = ""
    text = ""
