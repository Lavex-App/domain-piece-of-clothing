from typing import NamedTuple

from domain_piece_of_clothing.business.ports import (
    RemoveClothSpecificationInputPort,
    RemoveClothSpecificationOutputPort,
)

from ..services import ClothSpecificationService
from .interfaces import UseCase


class RemoveClothSpecificationServices(NamedTuple):
    cloth_specification_service: ClothSpecificationService


class RemoveClothSpecificationUseCase(UseCase):
    def __init__(self, services: RemoveClothSpecificationServices) -> None:
        self.__services = services

    async def __call__(self, input_port: RemoveClothSpecificationInputPort) -> RemoveClothSpecificationOutputPort:
        await self.__services.cloth_specification_service.delete(input_port.id, input_port.cloth_specification_id)
        return RemoveClothSpecificationOutputPort(msg="deleted")
