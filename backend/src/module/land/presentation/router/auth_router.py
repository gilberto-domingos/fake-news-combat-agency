from fastapi import APIRouter, Depends, status
from shared_infrastructure.dependency.land_dependency import get_command_mediator
from src.module.land.application.command.user_create_cmm import CreateUserCommand
from src.module.land.application.dto.user_crt_dto import CreateUserDto
from src.module.land.application.dto.user_res_dto import ResponseUserDto
from src.module.land.application.mediator.comm_mediator import CommandMediator

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
        mediator: CommandMediator = Depends(get_command_mediator)
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
        terms_accepted=user.terms_accepted,
        created_at=user.created_at,
    )
