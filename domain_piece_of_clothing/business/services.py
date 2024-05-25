from abc import ABCMeta, abstractmethod

from domain_piece_of_clothing.models.piece_of_clothing import PieceOfClothingModel


class PieceOfClothingService(metaclass=ABCMeta):
    @abstractmethod
    async def register(self, piece_of_cloting: PieceOfClothingModel) -> None: ...

    @abstractmethod
    async def find_by_id(self, piece_of_cloting_id: str) -> PieceOfClothingModel: ...
