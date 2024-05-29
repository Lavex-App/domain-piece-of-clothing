from domain_piece_of_clothing.models import PieceOfClothingIdModel, PieceOfClothingModel

from .interfaces import InputDTO, OutputDTO


class RegisterPieceOfClothingInputDTO(InputDTO, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputDTO(OutputDTO, PieceOfClothingIdModel):
    msg: str
