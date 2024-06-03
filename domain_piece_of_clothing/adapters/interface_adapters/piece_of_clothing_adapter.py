from math import ceil
from typing import Any, NamedTuple, cast

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.results import InsertOneResult

from domain_piece_of_clothing.business.ports import RetrieveClothesInputPort
from domain_piece_of_clothing.business.services import PieceOfClothingService
from domain_piece_of_clothing.models import (
    PaginationModel,
    PieceOfClothingFilterModel,
    PieceOfClothingIdModel,
    PieceOfClothingItems,
    PieceOfClothingModel,
    PieceOfClothingSortModel,
)

from .exceptions import CouldNotPerformDatabaseOperationException, DocumentIdNotFoundException
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
        piece_of_clothing_dict = piece_of_clothing.model_dump()
        piece_of_clothing_dict["specifications"] = [
            {**specification, "id": str(i)}
            for i, specification in enumerate(piece_of_clothing_dict["specifications"], start=1)
        ]
        insertion_result: InsertOneResult = await self.__cloths_collection.insert_one(piece_of_clothing_dict)
        if insertion_result.inserted_id:
            return PieceOfClothingIdModel(id=str(insertion_result.inserted_id), **piece_of_clothing_dict)
        raise CouldNotPerformDatabaseOperationException()

    async def delete(self, piece_of_clothing_id: str) -> None:
        result = await self.__cloths_collection.delete_one({"_id": ObjectId(piece_of_clothing_id)})
        if result.deleted_count == 0:
            raise DocumentIdNotFoundException()
        return None

    async def find_all_by_filter_and_pagination(self, input_port: RetrieveClothesInputPort) -> PieceOfClothingItems:
        query_filter = _PipelineMatch(input_port.filter).build()
        total_items: int = await self.__cloths_collection.count_documents(query_filter)
        if total_items == 0:
            return PieceOfClothingItems(
                current_page=input_port.pagination.page,
                total_pages=input_port.pagination.page,
                total_items=total_items,
                items=[],
            )

        pipeline = _PipelineBuilder(
            query_filter,
            _PipelineSort(input_port.sort).build(),
            _PipelinePagination(input_port.pagination).build(),
        )

        aggregate_result: dict = await self.__cloths_collection.aggregate(pipeline.build()).next()
        piece_of_clothing_result: dict = aggregate_result["data"]
        piece_of_clothing_list = [
            PieceOfClothingIdModel(**piece_of_clothing, id=str(piece_of_clothing["_id"]))
            for piece_of_clothing in piece_of_clothing_result
        ]
        total_pages = ceil(total_items / input_port.pagination.items_per_page)
        return PieceOfClothingItems(
            current_page=input_port.pagination.page,
            total_pages=total_pages,
            total_items=total_items,
            items=piece_of_clothing_list,
        )


class _PipelineBuilder:
    def __init__(self, query_match: dict, query_sort: dict, query_pagination: dict) -> None:
        self.__query_match = query_match
        self.__query_sort = query_sort
        self.__query_pagination = query_pagination

    def build(self) -> list[dict[str, Any]]:
        pipeline = []
        if self.__query_match:
            pipeline.append({"$match": self.__query_match})
        if self.__query_sort:
            pipeline.append({"$sort": self.__query_sort})
        if self.__query_pagination:
            pipeline.append(self.__query_pagination)
        return pipeline


class _PipelineMatch:
    def __init__(self, searching_filter: PieceOfClothingFilterModel) -> None:
        self.__searching_filter = searching_filter

    def build(self) -> dict[str, list[dict]]:
        search_match: dict[str, list[dict]] = {"$and": []}
        for key_name in self.__searching_filter.model_dump(exclude_none=True):
            query: dict = cast(dict, self.__searching_filter.structure_in_query(key_name))
            search_match["$and"].append(query)
        if not search_match["$and"]:
            return {}
        return search_match


class _PipelineSort:
    def __init__(self, searching_sort: PieceOfClothingSortModel) -> None:
        self.__searching_sort = searching_sort

    def build(self) -> dict[str, list[dict]]:
        return self.__searching_sort.model_dump(exclude_none=True)


class _PipelinePagination:
    def __init__(self, searching_pagination: PaginationModel) -> None:
        self.__searching_pagination = searching_pagination

    def build(self) -> dict[str, dict]:
        documents_to_skip = (self.__searching_pagination.page - 1) * self.__searching_pagination.items_per_page
        return {
            "$facet": {
                "metadata": [{"$count": "total"}, {"$addFields": {"page": self.__searching_pagination.page}}],
                "data": [{"$skip": documents_to_skip}, {"$limit": self.__searching_pagination.items_per_page}],
            },
        }
