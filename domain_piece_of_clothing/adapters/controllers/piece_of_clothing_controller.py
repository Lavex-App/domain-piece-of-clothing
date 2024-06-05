from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from domain_piece_of_clothing.business.ports import (
    RegisterPieceOfClothingInputPort,
    RemovePieceOfClothingInputPort,
    RetrieveClothesInputPort,
    UpdatePieceOfClothingInputPort,
)

from ..interface_adapters.exceptions import InterfaceAdaptersException
from .__dependencies__ import ControllerDependencies, FilterAndPaginationControllerDependencies
from .dtos import (
    RegisterPieceOfClothingInputDTO,
    RegisterPieceOfClothingOutputDTO,
    RemovePieceOfClothingOutputDTO,
    RetrieveClothesOutputDTO,
    UpdatePieceOfClothesInputDTO,
    UpdatePieceOfClothesOutputDTO,
)

piece_of_clothing_controller = APIRouter(prefix="/clothing", tags=["Piece of Clothing"])


@piece_of_clothing_controller.post(
    "/",
    response_model=RegisterPieceOfClothingOutputDTO,
    status_code=status.HTTP_201_CREATED,
)
async def register_piece_of_clothing(
    input_dto: RegisterPieceOfClothingInputDTO,
    dependencies: Annotated[ControllerDependencies, Depends()],
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
    dependencies: Annotated[FilterAndPaginationControllerDependencies, Depends()],
) -> RetrieveClothesOutputDTO:
    input_port = RetrieveClothesInputPort(
        filter=dependencies.filtering_model,
        pagination=dependencies.pagination_model,
        sort=dependencies.sorting_model,
    )
    output_port = await dependencies.retrieve_clothes_use_case(input_port=input_port)
    return RetrieveClothesOutputDTO(**output_port.model_dump())


@piece_of_clothing_controller.delete(
    "/{piece_of_clothing_id}",
    response_model=RemovePieceOfClothingOutputDTO,
    status_code=status.HTTP_200_OK,
)
async def remove_piece_of_clothing(
    piece_of_clothing_id: str,
    dependencies: Annotated[ControllerDependencies, Depends()],
) -> RemovePieceOfClothingOutputDTO | JSONResponse:
    input_port = RemovePieceOfClothingInputPort(id=piece_of_clothing_id)
    try:
        output_port = await dependencies.remove_piece_of_clothing_use_case(input_port=input_port)
    except InterfaceAdaptersException as error:
        return JSONResponse(content={"error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)
    return RemovePieceOfClothingOutputDTO(**output_port.model_dump())


@piece_of_clothing_controller.patch(
    "/{piece_of_clothing_id}",
    response_model=UpdatePieceOfClothesOutputDTO,
    status_code=status.HTTP_200_OK,
)
async def update_piece_of_clothing(
    piece_of_clothing_id: str,
    input_dto: UpdatePieceOfClothesInputDTO,
    dependencies: Annotated[ControllerDependencies, Depends()],
) -> UpdatePieceOfClothesOutputDTO | JSONResponse:
    input_port = UpdatePieceOfClothingInputPort(id=piece_of_clothing_id, **input_dto.model_dump())
    try:
        output_port = await dependencies.update_piece_of_clothing(input_port=input_port)
    except InterfaceAdaptersException as error:
        return JSONResponse(content={"error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)
    return UpdatePieceOfClothesOutputDTO(**output_port.model_dump())
