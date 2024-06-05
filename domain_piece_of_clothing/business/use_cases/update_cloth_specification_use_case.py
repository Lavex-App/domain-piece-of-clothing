from typing import NamedTuple

from domain_piece_of_clothing.business.ports import (
    UpdateClothSpecificationInputPort,
    UpdateClothSpecificationOutputPort,
)

from ..services import ClothSpecificationService
from .interfaces import UseCase


class UpdateClothSpecificationServices(NamedTuple):
    cloth_specification_service: ClothSpecificationService


class UpdateClothSpecificationUseCase(UseCase):
    def __init__(self, services: UpdateClothSpecificationServices) -> None:
        self.__services = services

    async def __call__(self, input_port: UpdateClothSpecificationInputPort) -> UpdateClothSpecificationOutputPort:
        await self.__services.cloth_specification_service.update(
            input_port.id,
            input_port.cloth_specification_id,
            input_port.cloth_specification_update,
        )
        return UpdateClothSpecificationOutputPort(msg="updated")
