from domain_piece_of_clothing.models import (
    ClothSpecificationIdModel,
    ClothSpecificationModel,
    ClothSpecificationUpdateModel,
    PaginationModel,
    PieceOfClothingFilterModel,
    PieceOfClothingIdModel,
    PieceOfClothingItems,
    PieceOfClothingModel,
    PieceOfClothingSortModel,
    PieceOfClothingUpdateModel,
)

from .interfaces import InputPort, OutputPort


class RegisterPieceOfClothingInputPort(InputPort, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputPort(OutputPort, PieceOfClothingIdModel):
    msg: str


class RetrieveClothesInputPort(InputPort):
    filter: PieceOfClothingFilterModel
    pagination: PaginationModel
    sort: PieceOfClothingSortModel


class RetrieveClothesOutputPort(OutputPort, PieceOfClothingItems):
    msg: str


class RemovePieceOfClothingInputPort(OutputPort):
    id: str


class RemovePieceOfClothingOutputPort(OutputPort):
    msg: str


class UpdatePieceOfClothingInputPort(OutputPort, PieceOfClothingUpdateModel):
    id: str


class UpdatePieceOfClothingOutputPort(OutputPort):
    msg: str


class AddClothSpecificationInputPort(InputPort):
    specifications: list[ClothSpecificationModel]
    id: str


class AddClothSpecificationOutputPort(OutputPort):
    added_specifications: list[ClothSpecificationIdModel]
    msg: str


class RemoveClothSpecificationInputPort(InputPort):
    id: str
    cloth_specification_id: str


class RemoveClothSpecificationOutputPort(OutputPort):
    msg: str


class UpdateClothSpecificationInputPort(InputPort):
    id: str
    cloth_specification_id: str
    cloth_specification_update: ClothSpecificationUpdateModel


class UpdateClothSpecificationOutputPort(OutputPort):
    msg: str
