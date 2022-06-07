#!/usr/bin/python3
"""The Class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel of the project"""
    def __init__(self, *args, **kwargs):
        """initializes a new instance of BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        """updates to the current time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return BaseModel instance
        
        includes key/value/__class__
        """
        rdict = self.__dict__.copy()
        rdict['__class__'] = self.__class__.__name__
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['created_at'] = self.created_at.isoformat()
        return rdict

    def __str__(self):
        """returns a string from the BaseModel instance"""
        namez = self.__class__.__name__
        return "[{}] ({}) {}".format(
            namez, self.id, self.__dict__)
