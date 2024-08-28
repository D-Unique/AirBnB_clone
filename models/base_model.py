#!/usr/bin/python3
'''base_model module'''
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    a class BaseModel that defines all
    common attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime

        """
        isintan = self.__dict__.copy()
        isintan["__class__"] = self.__class__.__name__
        isintan["updated_at"] = self.updated_at.isoformat()
        isintan["created_at"] = self.created_at.isoformat()
        return isintan

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89

    print("Initial Model:")
    print(my_model)

    my_model.save()
    print("\nModel After Updates:")
    print(my_model)

    my_model_json = my_model.to_dict()
    print("\nModel as Dictionary:")
    print(my_model_json)

    print("\nJSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}"
              .format(key, type(my_model_json[key]), my_model_json[key]))
