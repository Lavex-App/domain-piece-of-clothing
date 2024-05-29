from typing import Annotated

from fastapi import APIRouter, Depends, status

from domain_piece_of_clothing.business.ports import RegisterPieceOfClothingInputPort, RetrieveClothesInputPort

from .__dependencies__ import (
    PieceOfClothingControllerDependencies,
    PieceOfClothingWithFilterAndPaginationControllerDependencies,
)
from .dtos import RegisterPieceOfClothingInputDTO, RegisterPieceOfClothingOutputDTO, RetrieveClothesOutputDTO

piece_of_clothing_controller = APIRouter(prefix="/clothing")


@piece_of_clothing_controller.post(
    "/",
    response_model=RegisterPieceOfClothingOutputDTO,
    status_code=status.HTTP_201_CREATED,
)
async def register_piece_of_clothing(
    input_dto: RegisterPieceOfClothingInputDTO,
    dependencies: Annotated[PieceOfClothingControllerDependencies, Depends()],
) -> RegisterPieceOfClothingOutputDTO:
    input_port = RegisterPieceOfClothingInputPort(**input_dto.model_dump())
    output_port = await dependencies.register_piece_of_clothing_use_case(input_port=input_port)
    return RegisterPieceOfClothingOutputDTO(**output_port.model_dump())


@piece_of_clothing_controller.get(
    "/",
    response_model=RetrieveClothesOutputDTO,
    status_code=status.HTTP_200_OK,
)
async def retrieve_clothes(
    dependencies: Annotated[PieceOfClothingWithFilterAndPaginationControllerDependencies, Depends()],
) -> RetrieveClothesOutputDTO:
    input_port = RetrieveClothesInputPort(
        filter=dependencies.filtering_model,
        pagination=dependencies.pagination_model,
        sort=dependencies.sorting_model,
    )
    output_port = await dependencies.retrieve_clothes_use_case(input_port=input_port)
    return RetrieveClothesOutputDTO(**output_port.model_dump())
