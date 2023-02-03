#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel Class for AirBnb project"""


class BaseModel:
    """creating the base class for the project"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['created_at'] = self.created_at.isoformt()
        result['updated_at'] = self.updated_at.isoformat()
        return result