from abc import ABCMeta, abstractmethod

from domain_piece_of_clothing.models import (
    ClothSpecificationIdModel,
    ClothSpecificationModel,
    ClothSpecificationUpdateModel,
    PieceOfClothingIdModel,
    PieceOfClothingItems,
    PieceOfClothingModel,
    PieceOfClothingUpdateModel,
)

from .ports import RetrieveClothesInputPort


class PieceOfClothingService(metaclass=ABCMeta):
    @abstractmethod
    async def register(self, piece_of_clothing: PieceOfClothingModel) -> PieceOfClothingIdModel: ...

    @abstractmethod
    async def find_all_by_filter_and_pagination(self, input_port: RetrieveClothesInputPort) -> PieceOfClothingItems: ...

    @abstractmethod
    async def delete(self, piece_of_clothing_id: str) -> None: ...

    @abstractmethod
    async def update(self, piece_of_clothing_id: str, piece_of_clothing_update: PieceOfClothingUpdateModel) -> None: ...


class ClothSpecificationService(metaclass=ABCMeta):
    @abstractmethod
    async def add_all(
        self,
        piece_of_clothing_id: str,
        cloth_specifications: list[ClothSpecificationModel],
    ) -> list[ClothSpecificationIdModel]: ...

    @abstractmethod
    async def delete(self, piece_of_clothing_id: str, cloth_specification_id: str) -> None: ...

    @abstractmethod
    async def update(
        self,
        piece_of_clothing_id: str,
        cloth_specification_id: str,
        cloth_specification_update: ClothSpecificationUpdateModel,
    ) -> None: ...
