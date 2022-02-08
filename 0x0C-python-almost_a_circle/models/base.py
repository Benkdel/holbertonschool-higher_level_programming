#!/usr/bin/python3
"""
    Class Base
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
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Saves JSON string to file
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is None or not list_objs:
            pass
        else:
            for instance in list_objs:
                list_dict.append(instance.to_dictionary())

        json_str = cls.to_json_string(list_dict)

        with open(filename, mode="w") as filejson:
            filejson.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
            Returns:
                list of JSON string
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns:
                an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_object = cls(1, 1)
        elif cls.__name__ == "Square":
            new_object = cls(1)
        new_object.update(**dictionary)
        return new_object

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method: That writes the CSV string representation
            of list_objs to a file.
            Args:
                cls (class): The class.
                list_objs (list): Is a list of instances who inherits of Base.
                                  Example:
                                  list of Rectangle or list of Square instances
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w") as filecsv:
            if list_objs is not None and list_objs:
                if cls.__name__ == "Rectangle":
                    labels = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    labels = ["id", "size", "x", "y"]
                writer = csv.DictWriter(filecsv, fieldnames=labels)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Method: Create a list of instances.
            Returns:
                List of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        if os.path.isfile(filename) is False:
            return (list())

        with open(filename, mode="r") as filecsv:
            if cls.__name__ == "Rectangle":
                labels = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                labels = ["id", "size", "x", "y"]
            reader = csv.DictReader(filecsv, fieldnames=labels)

            """ Info - Convert str a int the values """
            list_dict = [dict([key, int(value)] for key, value in dic.items())
                         for dic in reader]
            list_inst = list()

            for dic in list_dict:
                list_inst.append(cls.create(**dic))

        return (list_inst)
