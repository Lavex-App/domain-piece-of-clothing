from domain_piece_of_clothing.models import PieceOfClothingModel

from .interfaces import InputPort, OutputPort


class RegisterPieceOfClothingInputPort(InputPort, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputPort(OutputPort):
    id: str
