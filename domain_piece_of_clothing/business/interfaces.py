from abc import ABCMeta

import bson
from pydantic import BaseModel

from domain_piece_of_clothing.types.object_id import ObjectId


class Service(metaclass=ABCMeta): ...


class Port(BaseModel, metaclass=ABCMeta):
    class Config:
        extra = "ignore"
        json_encoders = {bson.ObjectId: str, ObjectId: str}


class InputPort(Port, metaclass=ABCMeta): ...


class OutputPort(Port, metaclass=ABCMeta): ...
