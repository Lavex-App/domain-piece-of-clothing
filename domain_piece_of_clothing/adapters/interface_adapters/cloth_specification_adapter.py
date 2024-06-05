from typing import NamedTuple

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from domain_piece_of_clothing.business.services import ClothSpecificationService
from domain_piece_of_clothing.models import ClothSpecificationIdModel, ClothSpecificationModel

from .exceptions import DatabaseOperationNotAllowedException, DocumentIdNotFoundException
from .interfaces import DatabaseName, DocumentDatabaseProvider, InterfaceAdapter

ProviderType = DocumentDatabaseProvider[AsyncIOMotorClient, AsyncIOMotorDatabase]


class ClothSpecificationProviders(NamedTuple):
    document_database_provider: ProviderType


class ClothSpecificationAdapter(InterfaceAdapter, ClothSpecificationService):
    def __init__(self, providers: ClothSpecificationProviders) -> None:
        database_provider = providers.document_database_provider
        database_provider.database = DatabaseName.PIECE_OF_CLOTHING  # type: ignore
        self.__cloths_collection = database_provider.database["clothes"]

    async def add_all(
        self,
        piece_of_clothing_id: str,
        cloth_specifications: list[ClothSpecificationModel],
    ) -> list[ClothSpecificationIdModel]:
        update_filter = {"_id": ObjectId(piece_of_clothing_id)}
        found_piece_of_clothing = await self.__cloths_collection.find_one(update_filter)
        if not found_piece_of_clothing:
            raise DocumentIdNotFoundException()
        max_specification_id = max((specification["id"] for specification in found_piece_of_clothing["specifications"]))
        new_specifications = [
            {"id": str(cloth_specification_id), **cloth_specification.model_dump()}
            for cloth_specification_id, cloth_specification in enumerate(
                cloth_specifications, start=int(max_specification_id) + 1
            )
        ]
        insertions = {"$push": {"specifications": {"$each": new_specifications, "$sort": {"id": 1}}}}
        result = await self.__cloths_collection.update_one(update_filter, insertions)
        if not result.modified_count:
            raise DatabaseOperationNotAllowedException()
        return [ClothSpecificationIdModel(**specification) for specification in new_specifications]

    async def delete(self, piece_of_clothing_id: str, cloth_specification_id: str) -> None:
        deletition_filter = {"_id": ObjectId(piece_of_clothing_id)}
        deletition_query = {"$pull": {"specifications": {"id": cloth_specification_id}}}
        result = await self.__cloths_collection.update_one(deletition_filter, deletition_query)
        if result.modified_count == 0:
            raise DocumentIdNotFoundException()
        return None
