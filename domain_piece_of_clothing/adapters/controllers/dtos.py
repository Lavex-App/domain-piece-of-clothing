from domain_piece_of_clothing.models import (
    ClothSpecificationIdModel,
    ClothSpecificationModel,
    PieceOfClothingIdModel,
    PieceOfClothingItems,
    PieceOfClothingModel,
    PieceOfClothingUpdateModel,
)

from .interfaces import InputDTO, OutputDTO


class RegisterPieceOfClothingInputDTO(InputDTO, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputDTO(OutputDTO, PieceOfClothingIdModel):
    msg: str


class RetrieveClothesOutputDTO(OutputDTO, PieceOfClothingItems):
    msg: str


class RemovePieceOfClothingOutputDTO(OutputDTO):
    msg: str


class UpdatePieceOfClothesInputDTO(InputDTO, PieceOfClothingUpdateModel): ...


class UpdatePieceOfClothesOutputDTO(OutputDTO):
    msg: str


class AddClothSpecificationInputDTO(InputDTO):
    specifications: list[ClothSpecificationModel]


class AddClothSpecificationOutputDTO(OutputDTO):
    added_specifications: list[ClothSpecificationIdModel]
    msg: str
