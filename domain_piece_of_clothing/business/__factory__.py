from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from .services import PieceOfClothingService
from .use_cases import (
    RegisterPieceOfClothingServices,
    RegisterPieceOfClothingUseCase,
    RemovePieceOfClothingServices,
    RemovePieceOfClothingUseCase,
    RetrieveClothesServices,
    RetrieveClothesUseCase,
    UpdatePieceOfClothingServices,
    UpdatePieceOfClothingUseCase,
)

T_persist_piece_of_clothing_service_co = TypeVar(
    "T_persist_piece_of_clothing_service_co", bound=PieceOfClothingService, covariant=True
)


class AdaptersFactoryInterface(Generic[T_persist_piece_of_clothing_service_co], metaclass=ABCMeta):
    @abstractmethod
    def piece_of_clothing_service(self) -> T_persist_piece_of_clothing_service_co: ...


class BusinessFactory:
    def __init__(self, adapters_factory: AdaptersFactoryInterface) -> None:
        self.__factory = adapters_factory

    def register_piece_of_clothing_use_case(self) -> RegisterPieceOfClothingUseCase:
        services = RegisterPieceOfClothingServices(piece_of_clothing_service=self.__piece_of_clothing_service)
        return RegisterPieceOfClothingUseCase(services=services)

    def remove_piece_of_clothing_use_case(self) -> RemovePieceOfClothingUseCase:
        services = RemovePieceOfClothingServices(piece_of_clothing_service=self.__piece_of_clothing_service)
        return RemovePieceOfClothingUseCase(services=services)

    def update_piece_of_clothing_use_case(self) -> UpdatePieceOfClothingUseCase:
        services = UpdatePieceOfClothingServices(piece_of_clothing_service=self.__piece_of_clothing_service)
        return UpdatePieceOfClothingUseCase(services=services)

    def retrieve_clothes_use_case(self) -> RetrieveClothesUseCase:
        services = RetrieveClothesServices(piece_of_clothing_service=self.__piece_of_clothing_service)
        return RetrieveClothesUseCase(services=services)

    @property
    def __piece_of_clothing_service(self) -> PieceOfClothingService:
        return self.__factory.piece_of_clothing_service()
