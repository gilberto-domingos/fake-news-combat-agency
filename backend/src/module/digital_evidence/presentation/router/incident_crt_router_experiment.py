from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.command.incident_crt_cmd import IncidentCrtCommand
from src.module.digital_evidence.application.dto.incident_crt_dto_experiment import IncidentCrtDtoExperiment
from src.module.digital_evidence.application.dto.incident_res_dto import IncidentResDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from shared_infrastructure.dependencie.digital_evidence_dependencie import get_command_mediator

router = APIRouter()


@router.post("/", response_model=IncidentResDto, status_code=status.HTTP_201_CREATED)
async def create_incident(
        payload: IncidentCrtDtoExperiment,
        mediator: CommandMediator = Depends(get_command_mediator)
):
    command = IncidentCrtCommand(
        **payload.model_dump()
    )
    
    incident = await mediator.send(command)

    return incident
