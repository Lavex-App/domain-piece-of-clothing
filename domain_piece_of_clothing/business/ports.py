from domain_piece_of_clothing.models import (
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
