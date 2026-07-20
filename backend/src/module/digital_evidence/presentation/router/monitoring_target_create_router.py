from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.command.monitoring_target_create_cmd import MonitoringTargetCreateCommand
from src.module.digital_evidence.application.dto.monitoring_target_create_dto import MonitoringTargetCreateDto
from src.module.digital_evidence.application.dto.monitoring_target_response_dto import MonitoringTargetResponseDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from shared_infrastructure.dependency.digital_evidence_dependency import get_command_mediator

router = APIRouter(prefix="/monitoring_target", tags=["MonitoringTarget"])


@router.post("/", response_model=MonitoringTargetResponseDto, status_code=status.HTTP_201_CREATED)
async def create_monitoring_target(
        payload: MonitoringTargetCreateDto,
        mediator: CommandMediator = Depends(get_command_mediator)
):
    command = MonitoringTargetCreateCommand(
        **payload.model_dump()
    )

    monitoring_target = await mediator.send(command)

    return monitoring_target
