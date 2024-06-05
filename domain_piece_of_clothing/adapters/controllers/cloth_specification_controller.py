from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from domain_piece_of_clothing.business.ports import AddClothSpecificationInputPort

from ..interface_adapters.exceptions import InterfaceAdaptersException
from .__dependencies__ import ControllerDependencies
from .dtos import AddClothSpecificationInputDTO, AddClothSpecificationOutputDTO

cloth_specification_controller = APIRouter(prefix="/clothing", tags=["Cloth Specification"])


@cloth_specification_controller.post(
    "/{piece_of_clothing_id}",
    response_model=AddClothSpecificationOutputDTO,
    status_code=status.HTTP_201_CREATED,
)
async def register_piece_of_clothing(
    piece_of_clothing_id: str,
    input_dto: AddClothSpecificationInputDTO,
    dependencies: Annotated[ControllerDependencies, Depends()],
) -> AddClothSpecificationOutputDTO | JSONResponse:
    input_port = AddClothSpecificationInputPort(id=piece_of_clothing_id, **input_dto.model_dump())
    try:
        output_port = await dependencies.add_cloth_specification_use_case(input_port=input_port)
    except InterfaceAdaptersException as error:
        return JSONResponse(content={"error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST)
    return AddClothSpecificationOutputDTO(**output_port.model_dump())
