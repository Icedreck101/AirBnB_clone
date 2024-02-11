#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    A class for managing file storage of objects in JSON format.
    """

    __file_path = "file.json"
    __objects = {}

    def add_obj(self, obj):
        """
        Adds an object to the storage.

        Args:
            obj: The object to add.
        """
        obj.class_name = obj.__class__.__name__
        key = "{}.{}".format(obj.class_name, obj.id)

        FileStorage.__objects[key] = obj

    def retrieve(self):
        """
        Retrieves all stored objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects
    
    def save(self):
        """
        Serializes the object dictionary to JSON format and saves it to a file.
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def deserialize(self):
        """
        Deserializes the JSON file and loads stored objects into memory.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, values in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        serial = eval(class_name)

                        instance = serial(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

