#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}
    
    
    def new(self, obj):
        """
        
        """

        key = "{}.{}".format( obj.__class__.__name__, obj.id)
        
        FileStorage.__objects[key] = obj



    def all(self):
        """

        """
        return FileStorage.__objects
    
    def save(self):
        """Serializes objects to JSON file."""
        with open(FileStorage.__file_path,'w', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)
            
    def reload(self):
        """Deserializes JSON file to populate objects."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    FileStorage.__objects = json.load(f)
                    for key, value in FileStorage.__objects.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass 
