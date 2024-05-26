from domain_piece_of_clothing.models import (
    PaginationModel,
    PieceOfClothingFilterModel,
    PieceOfClothingIdModel,
    PieceOfClothingItems,
    PieceOfClothingModel,
)

from .interfaces import InputPort, OutputPort


class RegisterPieceOfClothingInputPort(InputPort, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputPort(OutputPort, PieceOfClothingIdModel):
    msg: str


class RetrieveClothesInputPort(InputPort, PieceOfClothingFilterModel, PaginationModel): ...


class RetrieveClothesOutputPort(OutputPort, PieceOfClothingItems):
    msg: str
