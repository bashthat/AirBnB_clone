#!/usr/bin/python3
""" FileStorage class """
import datetime
import json
import os


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """
        Returns a dict of classes
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}

    def all(self):
        """Returns all objects"""

        return FileStorage.__objects

    def new(self, obj):
        """new object set to dictionary"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes to JSON file."""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes JSON file into __objects."""

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}

            FileStorage.__objects = obj_dict
