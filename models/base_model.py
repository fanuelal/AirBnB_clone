#!/usr/bin/python3
"""
Defining a class BaseModel that defines all common
attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage
<<<<<<< HEAD
=======

>>>>>>> models

class BaseModel:
    """
     ___         ___  __  ___   __   __   _    __
    |___|  /_\  |__  |__  |  | |  | |  | |  \ |__ |
    |___| /   \  __| |__  |  |_|  | |__| |__/ |__ |__
    """

    def __init__(self, *args, **kwargs):
        """
        initializing  the public attr of the instance after creation
        """

        dateFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
<<<<<<< HEAD
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
=======
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs is not None:
            for key,value in kwargs.items():
>>>>>>> models
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dateFormat)
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)

    def __str__(self):
        """
        return a stringified class
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance
        attribute updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        return dict representation of the obj
        """
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_repr["__class__"] = type(self).__name__
        """storage.__objects = dict_repr"""
        return dict_repr
