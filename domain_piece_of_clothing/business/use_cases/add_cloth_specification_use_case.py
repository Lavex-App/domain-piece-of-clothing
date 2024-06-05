from typing import NamedTuple

from domain_piece_of_clothing.business.ports import AddClothSpecificationInputPort, AddClothSpecificationOutputPort

from ..services import ClothSpecificationService
from .interfaces import UseCase


class AddClothSpecificationServices(NamedTuple):
    cloth_specification_service: ClothSpecificationService


class AddClothSpecificationUseCase(UseCase):
    def __init__(self, services: AddClothSpecificationServices) -> None:
        self.__services = services

    async def __call__(self, input_port: AddClothSpecificationInputPort) -> AddClothSpecificationOutputPort:
        model_result = await self.__services.cloth_specification_service.add_all(
            input_port.id, input_port.specifications
        )
        return AddClothSpecificationOutputPort(added_specifications=model_result, msg="ok")
