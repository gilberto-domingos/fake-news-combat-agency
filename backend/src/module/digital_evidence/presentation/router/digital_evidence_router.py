from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.command.digital_evidence_crt_comm import DigitalEvidenceCrtCommand
from src.module.digital_evidence.application.dto.evidence_crt_dto import EvidenceCrtDto
from src.module.digital_evidence.application.dto.evidence_res_dto import EvidenceResDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from shared_infrastructure.dependencie.digital_evidence_dependencie import get_command_mediator

router = APIRouter(prefix="/digital_evidence", tags=["Digital_evidence"])


@router.post("/", response_model=EvidenceResDto, status_code=status.HTTP_201_CREATED)
async def evidence(payload: EvidenceCrtDto, mediator: CommandMediator = Depends(get_command_mediator)):
    command = DigitalEvidenceCrtCommand(**payload.model_dump())
    evidence = await mediator.send(command)

    return EvidenceResDto(
        id=evidence.id,
        url=evidence.url,
        source=evidence.source,
        captured_at=evidence.caputred_at,
        status=evidence.status,
        hash=evidence.hash
    )
