from abc import ABCMeta, abstractmethod

from domain_piece_of_clothing.models import PieceOfClothingIdModel, PieceOfClothingItems, PieceOfClothingModel

from .ports import RetrieveClothesInputPort


class PieceOfClothingService(metaclass=ABCMeta):
    @abstractmethod
    async def register(self, piece_of_clothing: PieceOfClothingModel) -> PieceOfClothingIdModel: ...

    @abstractmethod
    async def find_all_by_filter_and_pagination(self, input_port: RetrieveClothesInputPort) -> PieceOfClothingItems: ...
