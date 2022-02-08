#!/usr/bin/python3
"""
    Base Class
"""

import json
import os.path
import csv


class Base:
    """
        Base Class
        Handles IDs for all children
    """
    __nb__objects = 0

    def __init__(self, id=None):
        """
            Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns:
                JSON string of list_dic...
        """
        if list_dictionaries is None or list_dictionaries[0] == None:
            return ("[]")

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Saves JSON string to file
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dict)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
            Returns:
                list of JSON string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns:
                an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            Returns:
                List of instances
        """
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except:
            return result
