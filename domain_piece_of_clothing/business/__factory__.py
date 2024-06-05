from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from .services import ClothSpecificationService, PieceOfClothingService
from .use_cases import (
    AddClothSpecificationServices,
    AddClothSpecificationUseCase,
    RegisterPieceOfClothingServices,
    RegisterPieceOfClothingUseCase,
    RemoveClothSpecificationServices,
    RemoveClothSpecificationUseCase,
    RemovePieceOfClothingServices,
    RemovePieceOfClothingUseCase,
    RetrieveClothesServices,
    RetrieveClothesUseCase,
    UpdateClothSpecificationServices,
    UpdateClothSpecificationUseCase,
    UpdatePieceOfClothingServices,
    UpdatePieceOfClothingUseCase,
)

T_piece_of_clothing_service_co = TypeVar("T_piece_of_clothing_service_co", bound=PieceOfClothingService, covariant=True)
T_cloth_specification_service_co = TypeVar(
    "T_cloth_specification_service_co", bound=ClothSpecificationService, covariant=True
)


class AdaptersFactoryInterface(
    Generic[
        T_piece_of_clothing_service_co,
        T_cloth_specification_service_co,
    ],
    metaclass=ABCMeta,
):
    @abstractmethod
    def piece_of_clothing_service(self) -> T_piece_of_clothing_service_co: ...

    @abstractmethod
    def cloth_specification_service(self) -> T_cloth_specification_service_co: ...


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

    def add_cloth_specification_use_case(self) -> AddClothSpecificationUseCase:
        services = AddClothSpecificationServices(cloth_specification_service=self.__cloth_specification_service)
        return AddClothSpecificationUseCase(services=services)

    def remove_cloth_specification_use_case(self) -> RemoveClothSpecificationUseCase:
        services = RemoveClothSpecificationServices(cloth_specification_service=self.__cloth_specification_service)
        return RemoveClothSpecificationUseCase(services=services)

    def update_cloth_specification_use_case(self) -> UpdateClothSpecificationUseCase:
        services = UpdateClothSpecificationServices(cloth_specification_service=self.__cloth_specification_service)
        return UpdateClothSpecificationUseCase(services=services)

    @property
    def __piece_of_clothing_service(self) -> PieceOfClothingService:
        return self.__factory.piece_of_clothing_service()

    @property
    def __cloth_specification_service(self) -> ClothSpecificationService:
        return self.__factory.cloth_specification_service()
