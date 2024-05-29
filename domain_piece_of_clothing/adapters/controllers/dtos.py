from domain_piece_of_clothing.models import PieceOfClothingIdModel, PieceOfClothingItems, PieceOfClothingModel

from .interfaces import InputDTO, OutputDTO


class RegisterPieceOfClothingInputDTO(InputDTO, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputDTO(OutputDTO, PieceOfClothingIdModel):
    msg: str


class RetrieveClothesOutputDTO(OutputDTO, PieceOfClothingItems):
    msg: str
