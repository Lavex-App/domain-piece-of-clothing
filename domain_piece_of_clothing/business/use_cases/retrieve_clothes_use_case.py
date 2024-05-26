from typing import NamedTuple

from domain_piece_of_clothing.business.ports import RetrieveClothesInputPort, RetrieveClothesOutputPort

from ..services import PieceOfClothingService
from .interfaces import UseCase


class RetrieveClothesServices(NamedTuple):
    piece_of_clothing_service: PieceOfClothingService


class RetrieveClothesUseCase(UseCase):
    def __init__(self, services: RetrieveClothesServices) -> None:
        self.__services = services

    async def __call__(self, input_port: RetrieveClothesInputPort) -> RetrieveClothesOutputPort:
        model_result = await self.__services.piece_of_clothing_service.find_all_by_filter_and_pagination(input_port)
        return RetrieveClothesOutputPort(**model_result.model_dump(), msg="ok")
