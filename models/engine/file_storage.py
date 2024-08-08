#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
class FileStorage():
    def _init__(self):
        __file_path = "file.json"
        __objects = {}

    def new(self, obj):

        key = "{}.{}".format( obj.__class__.__name__, obj.id)
        self.__objects[key] = obj



    def all(self):
        """

        """
        return self.__objects
    
    def save(self):
        """Serializes objects to JSON file."""
        with open(self.__file_path,'w') as f:
            json.dump(self.__objects, f)



def reload(self):
        """Deserializes JSON file to populate objects."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    class_name = key.split('.')[0]
                    
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass  #
