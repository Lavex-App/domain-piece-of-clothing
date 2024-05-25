from enum import Enum

from pydantic import BaseModel


class Gender(str, Enum):
    """Ipsum ipsum"""

    M = "male"
    F = "female"
    U = "unisex"


class SizeLabel(str, Enum):
    """Ipsum ipsum"""

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


class PieceOfClothingModel(BaseModel):
    """Ipsum ipsum"""

    name: str
    category: str
    subcategory: str
    specifications: list[ClothSpecificationModel]
