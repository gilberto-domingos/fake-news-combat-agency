from fastapi import APIRouter, Depends, status
from application.dtos.crt_user_dto import CreateUserDto
from application.dtos.res_user_dto import ResponseUserDto
from application.commands.create_user import CreateUserCommand
from application.mediators.mediator import Mediator
from api.dependencies import get_mediator

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/",
    response_model=ResponseUserDto,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
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
        created_at=user.created_at
    )