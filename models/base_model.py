#!/usr/bin/python3
'''base_model module'''

from datetime import datatime
from uuid import uuid4

Class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow
        self.updated_at = datetime.utcnow

    def __str__(self):
        long_string = (
                f'[{self.__class__.__name__}] {self.id}'
                '[{self.updated_at.isoform()}]'
                '[{self.created_at.isoform()}] {self.__dict__}'
                )
        return long_string

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        output = {}
        for key, value in self.__dict__.item():
            if isinstance(value, datatime):
                output[key] = value.isoform()
            else
            output(key) = value
            output['__class__'] = self.__class__.__name__
        return output
