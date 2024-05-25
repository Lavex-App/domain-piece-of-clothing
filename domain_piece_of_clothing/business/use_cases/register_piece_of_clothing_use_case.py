from typing import NamedTuple

from domain_piece_of_clothing.business.ports import RegisterPieceOfClothingInputPort, RegisterPieceOfClothingOutputPort

from ..services import PieceOfClothingService
from .interfaces import UseCase


class RegisterPieceOfClothingServices(NamedTuple):
    piece_of_clothing_service: PieceOfClothingService


class RegisterPieceOfClothingUseCase(UseCase):
    def __init__(self, services: RegisterPieceOfClothingServices) -> None:
        self.__services = services

    async def __call__(self, input_port: RegisterPieceOfClothingInputPort) -> RegisterPieceOfClothingOutputPort:
        output_port = await self.__services.piece_of_clothing_service.register(input_port)
        return output_port
