from abc import ABCMeta
from typing import Any

from domain_piece_of_clothing.business import BusinessFactory
from domain_piece_of_clothing.business.use_cases import RegisterPieceOfClothingUseCase


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


class _ControllerDependency(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._dependency_manager = _ControllerDependencyManager()


class PieceOfClothingControllerDependencies(_ControllerDependency):
    @property
    def register_piece_of_clothing_use_case(self) -> RegisterPieceOfClothingUseCase:
        return self.register_piece_of_clothing_use_case()
