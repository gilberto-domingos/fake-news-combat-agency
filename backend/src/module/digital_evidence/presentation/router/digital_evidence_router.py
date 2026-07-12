from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.command.digital_evidence_crt_comm import DigitalEvidenceCrtCommand
from src.module.digital_evidence.domain.entity.evidence import Evidence

from src.module.digital_evidence.application.dto.evidence_res_dto import EvidenceResDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from shared_infrastructure.dependencie.digital_evidence_dependencie import get_command_mediator

router = APIRouter(prefix="/digital_evidence", tags=["Digital_evidence"])


@router.post("/", response_model=EvidenceResDto, status_code=status.HTTP_201_CREATED)
async def evidence(payload: Evidence, mediator: CommandMediator = Depends(get_command_mediator)):
    command = DigitalEvidenceCrtCommand(**payload.model_dump())
    evidence_entity = await mediator.send(command)
    return EvidenceResDto(
        id=evidence_entity.id,
        url=evidence_entity.url,
        source=evidence_entity.source,
        captured_at=evidence_entity.captured_at,
        status=evidence_entity.status,
        hash=evidence_entity.hash
    )
