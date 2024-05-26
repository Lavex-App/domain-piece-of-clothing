from domain_piece_of_clothing.models import PieceOfClothingIdModel, PieceOfClothingModel

from .interfaces import InputPort, OutputPort


class RegisterPieceOfClothingInputPort(InputPort, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputPort(OutputPort, PieceOfClothingIdModel):
    msg: str
