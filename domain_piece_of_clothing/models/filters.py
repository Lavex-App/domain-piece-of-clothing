from typing import Optional

from pydantic import BaseModel

from .piece_of_clothing import Gender, PieceOfClothingModel, SizeLabel


class PieceOfClothingFilterModel(BaseModel):
    name: Optional[str]
    category: Optional[str]
    subcategory: Optional[str]
    gender: Optional[list[Gender]]
    size_label: Optional[list[SizeLabel]]
    weight: Optional[str]
    size: Optional[str]


class PaginationModel(BaseModel):
    page: int
    items_per_page: int


class PageModel(BaseModel):
    total_items: int
    total_pages: int
    current_page: int


class PieceOfClothingItems(PageModel):
    items: list[PieceOfClothingModel]
