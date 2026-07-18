from fastapi import APIRouter, Depends, status
from shared_infrastructure.dependency.land_dependency import get_command_mediator
from src.module.land.application.command.invest_create_cmm import InvestCreateCommand
from src.module.land.application.dto.invest_crt_dto import InvestCreateDto
from src.module.land.application.dto.invest_res_dto import InvestResponseDto
from src.module.land.application.mediator.comm_mediator import CommandMediator

router = APIRouter(prefix="/invest", tags=["Invest"])


@router.post("/", response_model=InvestResponseDto, status_code=status.HTTP_201_CREATED)
async def invest(payload: InvestCreateDto, mediator: CommandMediator = Depends(get_command_mediator)):
    command = InvestCreateCommand(**payload.model_dump())

    invests = await mediator.send(command)

    return InvestResponseDto(
        id=invests.id,
        name=invests.name,
        proposal=invests.proposal,
        email=invests.email.value,
        created_at=invests.created_at
    )
