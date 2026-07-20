from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.command.evidence_create_cmd import EvidenceCreateCommand
from src.module.digital_evidence.application.dto.evidence_create_dto_experiment import EvidenceCreateDto

from src.module.digital_evidence.application.dto.evidence_response_dto import EvidenceResponseDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from shared_infrastructure.dependency.digital_evidence_dependency import get_command_mediator

router = APIRouter(prefix="/evidence", tags=["Evidence"])


@router.post("/", response_model=EvidenceResponseDto, status_code=status.HTTP_201_CREATED)
async def evidence(payload: EvidenceCreateDto, mediator: CommandMediator = Depends(get_command_mediator)):
    command = EvidenceCreateCommand(**payload.model_dump())
    entity = await mediator.send(command)
    return EvidenceResponseDto(
        id=entity.id,
        incident_id=entity.incident_id,
        url=entity.url,
        source=entity.source,
        captured_at=entity.captured_at,
        status=entity.status,
        hash=entity.hash
    )
