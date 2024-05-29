from domain_piece_of_clothing.adapters.__factory__ import FramewokrsFactoryInterface

from .mongodb import MotorFrameworkConfig, MotorManager


class FrameworksConfig:
    def __init__(self, motor_framework_config: MotorFrameworkConfig) -> None:
        self.motor_framework_config = motor_framework_config


class FrameworksFactory(FramewokrsFactoryInterface[MotorManager]):
    def __init__(self, config: FrameworksConfig) -> None:
        self.__config = config
        self.__motor_manager = MotorManager(self.__config.motor_framework_config)

    async def connect(self) -> None:
        await self.__motor_manager.connect()

    def close(self) -> None:
        self.__motor_manager.close()

    def database_provider(self) -> MotorManager:
        return self.__motor_manager
