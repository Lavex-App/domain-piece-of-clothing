from typing import NamedTuple

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.results import InsertOneResult

from domain_piece_of_clothing.business.services import PieceOfClothingService
from domain_piece_of_clothing.models import PieceOfClothingIdModel, PieceOfClothingModel

from .exceptions import CouldNotPerformDatabaseOperation
from .interfaces import DatabaseName, DocumentDatabaseProvider, InterfaceAdapter

ProviderType = DocumentDatabaseProvider[AsyncIOMotorClient, AsyncIOMotorDatabase]


class PieceOfClothingProviders(NamedTuple):
    document_database_provider: ProviderType


class PieceOfClothingAdapter(InterfaceAdapter, PieceOfClothingService):
    def __init__(self, providers: PieceOfClothingProviders) -> None:
        database_provider = providers.document_database_provider
        database_provider.database = DatabaseName.PIECE_OF_CLOTHING  # type: ignore
        self.__cloths_collection = database_provider.database["clothes"]

    async def register(self, piece_of_clothing: PieceOfClothingModel) -> PieceOfClothingIdModel:
        insertion_result: InsertOneResult = await self.__cloths_collection.insert_one(piece_of_clothing.model_dump())
        if insertion_result.inserted_id:
            return PieceOfClothingIdModel(registered_piece_of_clothing_id=str(insertion_result.inserted_id))
        raise CouldNotPerformDatabaseOperation()
