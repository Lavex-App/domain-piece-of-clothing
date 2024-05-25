from abc import ABCMeta, abstractmethod

from domain_piece_of_clothing.models import PieceOfClothingModel


class PieceOfClothingService(metaclass=ABCMeta):
    @abstractmethod
    async def register(self, piece_of_clothing: PieceOfClothingModel) -> None: ...
