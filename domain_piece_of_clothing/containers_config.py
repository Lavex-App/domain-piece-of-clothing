from abc import ABCMeta
from functools import lru_cache

from environs import Env

from domain_piece_of_clothing.adapters.__factory__ import AdaptersFactory
from domain_piece_of_clothing.adapters.controllers.__dependencies__ import bind_controller_dependencies
from domain_piece_of_clothing.business.__factory__ import BusinessFactory
from domain_piece_of_clothing.frameworks.__factory__ import FrameworksConfig, FrameworksFactory
from domain_piece_of_clothing.frameworks.mongodb import MotorFrameworkConfig


class Config(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._env = Env(eager=True)
        self._env.read_env()

    @property
    @lru_cache
    def is_local(self) -> bool:
        return self._get_project_env == "local"

    @property
    @lru_cache
    def is_staging(self) -> bool:
        return self._get_project_env in ["dev", "staging"]

    @property
    @lru_cache
    def is_production(self) -> bool:
        return self._get_project_env == "main"

    @property
    @lru_cache
    def _get_project_env(self) -> str:
        return self._env.str("ENV", "main")


class ProjectConfig(Config):
    @property
    @lru_cache
    def frameworks_config(self) -> FrameworksConfig:
        return FrameworksConfig(motor_framework_config=self.__motor_framework_config)

    @property
    @lru_cache
    def __motor_framework_config(self) -> MotorFrameworkConfig:
        return MotorFrameworkConfig(
            database_uri=self._env.str("DB_URI"),
            service_name=self._env.str("SERVICE_NAME"),
            sandbox=self.is_local or self.is_staging,
        )


class AppBinding:
    business: BusinessFactory
    adapters: AdaptersFactory
    frameworks: FrameworksFactory

    def __init__(self, frameworks_config: FrameworksConfig) -> None:
        self.frameworks_config = frameworks_config

    def bind_frameworks(self) -> None:
        self.frameworks = FrameworksFactory(self.frameworks_config)

    def bind_adapters(self) -> None:
        self.adapters = AdaptersFactory(self.frameworks)

    def bind_business(self) -> None:
        self.business = BusinessFactory(self.adapters)

    def bind_controllers(self) -> None:
        bind_controller_dependencies(self.business)

    def facade(self) -> None:
        self.bind_frameworks()
        self.bind_adapters()
        self.bind_business()
        self.bind_controllers()
