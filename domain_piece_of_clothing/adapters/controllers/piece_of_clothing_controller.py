from typing import Annotated

from fastapi import APIRouter, Depends

from domain_piece_of_clothing.business.ports import RegisterPieceOfClothingInputPort

from .__dependencies__ import PieceOfClothingControllerDependencies
from .dtos import RegisterPieceOfClothingInputDTO, RegisterPieceOfClothingOutputDTO

piece_of_clothing_controller = APIRouter(prefix="/clothing")


@piece_of_clothing_controller.post("/", response_model=RegisterPieceOfClothingOutputDTO)
async def register_piece_of_clothing(
    input_dto: RegisterPieceOfClothingInputDTO,
    dependencies: Annotated[PieceOfClothingControllerDependencies, Depends()],
) -> RegisterPieceOfClothingOutputDTO:
    input_port = RegisterPieceOfClothingInputPort(**input_dto.model_dump())
    output_port = await dependencies.register_piece_of_clothing_use_case(input_port=input_port)
    return RegisterPieceOfClothingOutputDTO(**output_port.model_dump())
