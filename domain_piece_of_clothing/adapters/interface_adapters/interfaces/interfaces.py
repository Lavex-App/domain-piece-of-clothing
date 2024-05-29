from abc import ABCMeta, abstractmethod

from .document_database_provider import DocumentDatabaseProvider


class InterfaceAdapter(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *providers: DocumentDatabaseProvider) -> None: ...
