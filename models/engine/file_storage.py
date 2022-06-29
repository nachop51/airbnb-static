#!/usr/bin/python3
""" File Storage module """
import json
from os.path import exists


class FileStorage:
    """ File storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        serialized = {key: value.to_dict() for key,
                      value in FileStorage.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized, file)

    @staticmethod
    def classes():
        """ Returns a dict of classes """
        from models.base_model import BaseModel
        list_classes = {
            "BaseModel": BaseModel,
        }
        return list_classes

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if exists(self.__file_path):
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
            dummy = None
            for key, value in data.items():
                dummy = self.classes()[key.split('.')[0]](**value)
                FileStorage.__objects[key] = dummy
