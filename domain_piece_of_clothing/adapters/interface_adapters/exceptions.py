class InterfaceAdaptersException(RuntimeError):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.type = self.__class__.__name__
        self.msg = msg

    def __str__(self) -> str:
        return f"[{self.type}] {self.msg}"


class CouldNotPerformDatabaseOperationException(InterfaceAdaptersException):
    def __init__(self) -> None:
        super().__init__("System down, try again later")


class DocumentIdNotFoundException(InterfaceAdaptersException):
    def __init__(self) -> None:
        super().__init__("Could not find the document of the specified id")
