from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.command.monitoring_target_create_cmd import MonitoringTargetCrtCommand
from src.module.digital_evidence.application.dto.monitoring_target_create_dto import MonitoringTargetCrtDto
from src.module.digital_evidence.application.dto.monitoring_target_response_dto import MonitoringTargetResDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from shared_infrastructure.dependency.digital_evidence_dependency import get_command_mediator

router = APIRouter()


@router.post("/", response_model=MonitoringTargetResDto, status_code=status.HTTP_201_CREATED)
async def create_monitoring_target(
        payload: MonitoringTargetCrtDto,
        mediator: CommandMediator = Depends(get_command_mediator)
):
    command = MonitoringTargetCrtCommand(
        **payload.model_dump()
    )

    monitoring_target = await mediator.send(command)

    return monitoring_target
