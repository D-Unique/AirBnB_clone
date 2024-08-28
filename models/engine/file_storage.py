#!/usr/bin/python3
import json
import os


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to
 a JSON file (path: __file_path)"""

        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding='utf8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised).
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding='utf8') as f:
                data = json.load(f)
                try:
                    for key, value in data.items():
                        class_name, obj.id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        self.__objects[key] = instance
                except: pass
