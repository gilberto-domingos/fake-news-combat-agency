from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus
from src.module.digital_evidence.application.dto.evidence_snapshot_response_dto import EvidenceSnapshotResponseDto


class EvidenceDetailResponseDto(BaseModel):
    id: UUID
    incident_id: UUID
    url: str
    source: str
    captured_at: datetime
    status: EvidenceStatus
    hash: str
