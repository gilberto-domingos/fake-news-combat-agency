from fastapi import APIRouter, Depends, status

from src.api.dependencies import get_mediator
from src.application.command.create_user_cmm import CreateUserCommand
from src.application.dtos.crt_user_dto import CreateUserDto
from src.application.dtos.res_user_dto import ResponseUserDto
from src.application.mediators.mediator import Mediator

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/signup",
    response_model=ResponseUserDto,
    status_code=status.HTTP_201_CREATED
)
async def signup(
        payload: CreateUserDto,
        mediator: Mediator = Depends(get_mediator)
):
    command = CreateUserCommand(**payload.model_dump())

    user = await mediator.send(command)

    return ResponseUserDto(
        id=user.id,
        name=user.name,
        lastname=user.lastname,
        email=user.email.value,
        birthdate=user.birthdate,
        gender=user.gender,
        profession=user.profession,
        phone=user.phone,
        created_at=user.created_at,
    )
