from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from fastapi import FastAPI

from domain_piece_of_clothing.business import AdaptersFactoryInterface

from .controllers import Binding
from .interface_adapters import (
    ClothSpecificationAdapter,
    ClothSpecificationProviders,
    PieceOfClothingAdapter,
    PieceOfClothingProviders,
)
from .interface_adapters.interfaces import DocumentDatabaseProvider

T_database_co = TypeVar("T_database_co", bound=DocumentDatabaseProvider, covariant=True)


class FramewokrsFactoryInterface(Generic[T_database_co], metaclass=ABCMeta):
    @abstractmethod
    def database_provider(self) -> T_database_co: ...


class AdaptersFactory(
    AdaptersFactoryInterface[
        PieceOfClothingAdapter,
        ClothSpecificationAdapter,
    ]
):
    def __init__(self, frameworks_factory: FramewokrsFactoryInterface) -> None:
        self.__factory = frameworks_factory

    def piece_of_clothing_service(self) -> PieceOfClothingAdapter:
        providers = PieceOfClothingProviders(document_database_provider=self.__factory.database_provider())
        return PieceOfClothingAdapter(providers=providers)

    def cloth_specification_service(self) -> ClothSpecificationAdapter:
        providers = ClothSpecificationProviders(document_database_provider=self.__factory.database_provider())
        return ClothSpecificationAdapter(providers=providers)

    @staticmethod
    def register_routes(app: FastAPI) -> None:
        Binding().register_all(app)
