from enum import Enum

from pydantic import BaseModel


class Gender(str, Enum):
    M = "male"
    F = "female"
    U = "unisex"


class SizeLabel(str, Enum):
    XS = "pp"
    S = "p"
    M = "m"
    L = "g"
    XL = "gg"


class ClothSpecificationModel(BaseModel):
    gender: Gender
    size_label: SizeLabel
    size: int
    weight: int


class ClothSpecificationIdModel(BaseModel):
    id: str
    gender: Gender
    size_label: SizeLabel
    size: int
    weight: int


class PieceOfClothingModel(BaseModel):
    name: str
    category: str
    subcategory: str
    specifications: list[ClothSpecificationModel]


class PieceOfClothingIdModel(BaseModel):
    id: str
    name: str
    category: str
    subcategory: str
    specifications: list[ClothSpecificationIdModel]
