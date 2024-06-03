from typing import NamedTuple

from domain_piece_of_clothing.business.ports import RemovePieceOfClothingInputPort, RemovePieceOfClothingOutputPort

from ..services import PieceOfClothingService
from .interfaces import UseCase


class RemovePieceOfClothingServices(NamedTuple):
    piece_of_clothing_service: PieceOfClothingService


class RemovePieceOfClothingUseCase(UseCase):
    def __init__(self, services: RemovePieceOfClothingServices) -> None:
        self.__services = services

    async def __call__(self, input_port: RemovePieceOfClothingInputPort) -> RemovePieceOfClothingOutputPort:
        await self.__services.piece_of_clothing_service.delete(input_port.id)
        return RemovePieceOfClothingOutputPort(msg="deleted")
