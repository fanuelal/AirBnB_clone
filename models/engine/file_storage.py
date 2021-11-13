import json
from datetime import datetime
"""
FILE STORAGE IN JOSON FILE
"""
class FileStorage:
    """public attribute
    Attributes:
      __file_path (str): the path of the json file
      __objects (dict): A dictionary of instatiated obj
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary object"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with key"""
        
        self.__objects = self.obj
    def save(self):
        
        return  
    def reload(self):

        return self.__objects
