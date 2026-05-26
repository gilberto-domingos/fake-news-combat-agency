from fastapi import APIRouter, Depends, status
from src.api.dependencies import get_command_mediator
from src.application.command.invest_create_cmm import InvestCreateCommand
from src.application.dto.invest_crt_dto import InvestCreateDto
from src.application.dto.invest_res_dto import InvestResponseDto
from src.application.mediator.comm_mediator import CommandMediator

router = APIRouter(prefix="/invest", tags=["Invest"])


@router.post("/", response_model=InvestResponseDto, status_code=status.HTTP_201_CREATED)
async def invest(
        payload: InvestCreateDto,
        mediator: CommandMediator = Depends(get_command_mediator)
):
    command = InvestCreateCommand(**payload.model_dump())

    invests = await mediator.send(command)

    return InvestResponseDto(
        id=invests.id,
        name=invests.name,
        proposal=invests.proposal,
        email=invests.email.value,
        created_at=invests.created_at
    )
