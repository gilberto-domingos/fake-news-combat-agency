from fastapi import APIRouter, Depends, status

from src.api.dependencies import get_mediator
from src.application.command.create_user_cmm import CreateUserCommand
from src.application.command.access_counter_comm import AccessCounterCommand
from src.application.dtos.crt_user_dto import CreateUserDto
from src.application.dtos.res_user_dto import ResponseUserDto
from src.application.mediators.mediator import Mediator

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=ResponseUserDto, status_code=status.HTTP_201_CREATED)
async def create_user(
        payload: CreateUserDto,
        mediator: Mediator = Depends(get_mediator)
):
    command = CreateUserCommand(**payload.model_dump())
    access_command = AccessCounterCommand(access_counter=payload.access_counter)

    user = await mediator.send(command)
    access_counter = await mediator.send(access_command)

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
        access_counter=access_counter
    )
