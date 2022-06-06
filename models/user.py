#!/usr/bin/python3
"""Defines the User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents the User/user input or information
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
