from abc import ABCMeta, abstractmethod

from domain_piece_of_clothing.models import PieceOfClothingIdModel, PieceOfClothingModel


class PieceOfClothingService(metaclass=ABCMeta):
    @abstractmethod
    async def register(self, piece_of_clothing: PieceOfClothingModel) -> PieceOfClothingIdModel: ...
