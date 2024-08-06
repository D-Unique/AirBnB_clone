#!/usr/bin/python3
'''base_model module'''
from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        
        """
        self.updated_at = datetime.utcnow()

   # def to_dict(self):
    #    """
        
     #   """
      #  output = {}
       # for key, value in self.__dict__.item():
        #    if isinstance(value, datatime):
         #       output[key] = value.isoform()
          #  else:
          # output[key] = value
                #output['__class__'] = self.__class__.__name__
        #return output

    def to_dict(self):
        isintan = self.__dict__.copy()
        isintan["__class__"] = self.__class__.__name__
        isintan["updated_at"] = self.updated_at
        isintan["created_at"] = self.created_at
        return isintan
    def __str__(self):
        class_name = self.__class__.__name__
        return "{}, {}, {}".format(class_name, self.id, self.__dict__)


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
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
