from fastapi import APIRouter, Depends, status
from src.module.digital_evidence.application.dto.evidence_snapshot_response_dto import EvidenceSnapshotResponseDto
from src.module.digital_evidence.application.command.evidence_snapshot_create_cmd import EvidenceSnapshotCreateCommand
from src.module.digital_evidence.application.dto.evidence_snapshot_create_dto_experiment import \
    EvidenceSnapshotCreateDto
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator
from src.shared_infrastructure.dependency.digital_evidence_dependency import get_command_mediator

router = APIRouter(prefix="/evidence_snapshot", tags=["EvidenceSnapshot"])


@router.post("/", response_model=EvidenceSnapshotResponseDto, status_code=status.HTTP_201_CREATED)
async def create_snapshot(
        payload: EvidenceSnapshotCreateDto,
        mediator: CommandMediator = Depends(get_command_mediator)
):
    command = EvidenceSnapshotCreateCommand(
        **payload.model_dump()
    )

    evidence_snapshot = await mediator.send(command)
    return evidence_snapshot
