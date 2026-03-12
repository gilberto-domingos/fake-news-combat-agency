from fastapi import APIRouter, Depends, status
from src.api.dependencies import get_mediator
from src.application.mediators.mediator import Mediator
from src.application.command.access_counter_comm import AccessCounterCommand
from src.application.dtos.access_counter_dto import AccessCounterDto

router = APIRouter(prefix="/counter_access", tags=["CounterAccess"])


@router.post("/", response_model=AccessCounterDto, status_code=status.HTTP_201_CREATED)
async def create_access_counter(payload: AccessCounterDto, mediator: Mediator = Depends(get_mediator)):
    command = AccessCounterCommand(**payload.model_dump())

    count = await mediator.send(command)

    return AccessCounterDto(access_counter=count.access_counter)
