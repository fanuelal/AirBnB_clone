#!/usr/bin/python3
import json
from json import JSONEncoder
from datetime import datetime
import os

"""
FILE STORAGE IN JSON FILE
"""


class MyEncoder(JSONEncoder):
    """making a class json serializable"""
    def default(self, o):
        if isInstance(o, models.base_model.BaseModel):
            return o.to_dict()
        return super().default()


class FileStorage:
    """
    private Attributes:
    __file_path (str): the path of the json file
    __objects (dict): A dictionary of instatiated obj
    public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key"""

        if obj is not None:
            FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        serializes __objects to the JSON file(path: __file_path)
        """
        file = FileStorage.__file_path
        with open(file, 'w') as jsonFile:
            jsonFile.write(json.dumps(FileStorage.__objects, cls=MyEncoder))

    def reload(self):
        """
        deserializes the JSON file to __objects
        otherwise, do nothing.
        If the file doesn’t exist, no exception
        """
        file = FileStorage.__file_path

        try:
            with open(file, 'r') as jsonFile:
                """ deserialize json str into a dict"""
                dictObj = json.loads(jsonFile)
                for strObj in dictObj.values():
                    """calling a class instance from dict return"""
                    cls = eval(strObj['__class__'])
                    newObj = cls(**strObj)
                    self.new(newObj)
        except FileNotFoundError:
            return
