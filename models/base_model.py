#!/usr/bin/python3
"""The Class"""
import uuid
from datetime import datetime
from models import storage


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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates to the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return BaseModel instance
        
        includes key/value/__class__
        """
        dictionary = vars(self).copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['created_at'] = self.created_at.isoformat()
        return dictionary

    def __str__(self):
        """returns a string from the BaseModel instance"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)
