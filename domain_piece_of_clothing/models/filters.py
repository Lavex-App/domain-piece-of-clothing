from typing import Annotated, Optional

from pydantic import AfterValidator, BaseModel, ConfigDict

from .piece_of_clothing import Gender, PieceOfClothingIdModel, SizeLabel


class PieceOfClothingFilterModel(BaseModel):
    name: Optional[list[str]] = None
    category: Optional[list[str]] = None
    subcategory: Optional[list[str]] = None
    gender: Optional[list[Gender]] = None
    size_label: Optional[list[SizeLabel]] = None
    weight: Optional[list[int]] = None
    size: Optional[list[int]] = None

    def structure_in_query(self, key_name: str) -> dict | None:
        if (value := getattr(self, key_name, None)) is not None:
            if key_name in ["name", "category", "subcategory"]:
                return {key_name: {"$in": value}}
            if key_name in ["gender", "size_label"]:
                return {f"specifications.{key_name}": {"$in": [enum_value.value for enum_value in value]}}
            if key_name in ["weight", "size"]:
                query = {}
                query["$gt"] = value[0]
                if (highest_value := value[1] if len(value) == 2 else None) is not None:
                    query["$lt"] = highest_value
                return {f"specifications.{key_name}": query}
        return None


def check_is_filter_value(value: int) -> int:
    assert value in [1, -1], f"It is not possible to perform sorting with the value {value}"
    return value


FilterValue = Annotated[int, AfterValidator(check_is_filter_value)]


def add_sort_preffix(attr_name: str) -> str:
    return f"sort_by_{attr_name}"


class PieceOfClothingSortModel(BaseModel):
    model_config = ConfigDict(alias_generator=add_sort_preffix)

    name: Optional[FilterValue] = None
    category: Optional[FilterValue] = None
    subcategory: Optional[FilterValue] = None
    weight: Optional[FilterValue] = None
    size: Optional[FilterValue] = None


class PaginationModel(BaseModel):
    page: int = 1
    items_per_page: int = 50


class PageModel(BaseModel):
    total_items: int
    total_pages: int
    current_page: int


class PieceOfClothingItems(PageModel):
    items: list[PieceOfClothingIdModel]
