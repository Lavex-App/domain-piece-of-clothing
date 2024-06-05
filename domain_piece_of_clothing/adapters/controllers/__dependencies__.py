from abc import ABCMeta
from typing import Any, Optional

from fastapi import Depends, Query

from domain_piece_of_clothing.business import BusinessFactory
from domain_piece_of_clothing.business.use_cases import (
    AddClothSpecificationUseCase,
    RegisterPieceOfClothingUseCase,
    RemoveClothSpecificationUseCase,
    RemovePieceOfClothingUseCase,
    RetrieveClothesUseCase,
    UpdatePieceOfClothingUseCase,
)
from domain_piece_of_clothing.models import (
    Gender,
    PaginationModel,
    PieceOfClothingFilterModel,
    PieceOfClothingSortModel,
    SizeLabel,
)


def bind_controller_dependencies(business_factory: BusinessFactory) -> None:
    _ControllerDependencyManager(business_factory)


class ControllerDependencyManagerIsNotInitializedException(RuntimeError):
    def __init__(self) -> None:
        self.type = "Dependency Manager"
        self.msg = "Something is trying to use the ControllerDependencyManager without initialize it"
        super().__init__(self.msg)


class _Singleton(type):
    _instances: dict[type, object] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> object:
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class _ControllerDependencyManager(metaclass=_Singleton):
    def __init__(self, business_factory: BusinessFactory | None = None) -> None:
        if business_factory:
            self.__factory = business_factory

    def register_piece_of_clothing_use_case(self) -> RegisterPieceOfClothingUseCase:
        if self.__factory:
            return self.__factory.register_piece_of_clothing_use_case()
        raise ControllerDependencyManagerIsNotInitializedException()

    def remove_piece_of_clothing_use_case(self) -> RemovePieceOfClothingUseCase:
        if self.__factory:
            return self.__factory.remove_piece_of_clothing_use_case()
        raise ControllerDependencyManagerIsNotInitializedException()

    def update_piece_of_clothing_use_case(self) -> UpdatePieceOfClothingUseCase:
        if self.__factory:
            return self.__factory.update_piece_of_clothing_use_case()
        raise ControllerDependencyManagerIsNotInitializedException()

    def retrieve_clothes_use_case(self) -> RetrieveClothesUseCase:
        if self.__factory:
            return self.__factory.retrieve_clothes_use_case()
        raise ControllerDependencyManagerIsNotInitializedException()

    def add_cloth_specification_use_case(self) -> AddClothSpecificationUseCase:
        if self.__factory:
            return self.__factory.add_cloth_specification_use_case()
        raise ControllerDependencyManagerIsNotInitializedException()

    def remove_cloth_specification_use_case(self) -> RemoveClothSpecificationUseCase:
        if self.__factory:
            return self.__factory.remove_cloth_specification_use_case()
        raise ControllerDependencyManagerIsNotInitializedException()


class _ControllerDependency(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._dependency_manager = _ControllerDependencyManager()


class _FilterAndPaginationControllerDependency(_ControllerDependency):
    def __init__(
        self,
        pagination: PaginationModel = Depends(),
        sorting: PieceOfClothingSortModel = Depends(),
        name: Optional[list[str]] = Query(None),
        category: Optional[list[str]] = Query(None),
        subcategory: Optional[list[str]] = Query(None),
        gender: Optional[list[Gender]] = Query(None),
        size_label: Optional[list[SizeLabel]] = Query(None),
        weight: Optional[list[int]] = Query(None),
        size: Optional[list[int]] = Query(None),
    ) -> None:
        super().__init__()
        self.pagination_model = pagination
        self.sorting_model = sorting
        self.filtering_model = PieceOfClothingFilterModel(
            name=name,
            category=category,
            subcategory=subcategory,
            gender=gender,
            size_label=size_label,
            weight=weight,
            size=size,
        )


class ControllerDependencies(_ControllerDependency):
    @property
    def register_piece_of_clothing_use_case(self) -> RegisterPieceOfClothingUseCase:
        return self._dependency_manager.register_piece_of_clothing_use_case()

    @property
    def remove_piece_of_clothing_use_case(self) -> RemovePieceOfClothingUseCase:
        return self._dependency_manager.remove_piece_of_clothing_use_case()

    @property
    def update_piece_of_clothing(self) -> UpdatePieceOfClothingUseCase:
        return self._dependency_manager.update_piece_of_clothing_use_case()

    @property
    def add_cloth_specification_use_case(self) -> AddClothSpecificationUseCase:
        return self._dependency_manager.add_cloth_specification_use_case()

    @property
    def remove_cloth_specification_use_case(self) -> RemoveClothSpecificationUseCase:
        return self._dependency_manager.remove_cloth_specification_use_case()


class FilterAndPaginationControllerDependencies(_FilterAndPaginationControllerDependency):
    @property
    def retrieve_clothes_use_case(self) -> RetrieveClothesUseCase:
        return self._dependency_manager.retrieve_clothes_use_case()
