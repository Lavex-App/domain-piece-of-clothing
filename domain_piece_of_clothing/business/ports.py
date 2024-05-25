from domain_piece_of_clothing.models.piece_of_clothing import PieceOfClothingModel

from .interfaces import InputPort, OutputPort


class RegisterPieceOfClothingInputPort(InputPort, PieceOfClothingModel): ...


class RegisterPieceOfClothingOutputPort(OutputPort):
    id: str
