from typing import NamedTuple

from domain_piece_of_clothing.business.ports import UpdatePieceOfClothingInputPort, UpdatePieceOfClothingOutputPort
from domain_piece_of_clothing.models.piece_of_clothing import PieceOfClothingUpdateModel

from ..services import PieceOfClothingService
from .interfaces import UseCase


class UpdatePieceOfClothingServices(NamedTuple):
    piece_of_clothing_service: PieceOfClothingService


class UpdatePieceOfClothingUseCase(UseCase):
    def __init__(self, services: UpdatePieceOfClothingServices) -> None:
        self.__services = services

    async def __call__(self, input_port: UpdatePieceOfClothingInputPort) -> UpdatePieceOfClothingOutputPort:
        await self.__services.piece_of_clothing_service.update(input_port.id, PieceOfClothingUpdateModel(**input_port.model_dump(exclude_none=True)))
        return UpdatePieceOfClothingOutputPort(msg="updated")
