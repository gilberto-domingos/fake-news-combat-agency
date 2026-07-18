from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus


class EvidenceCreateDto(BaseModel):
    incident_id: UUID
    url: str
    source: str
    captured_at: datetime
    status: EvidenceStatus
    hash: str

    model_config = {
        "from_attributes": True
    }
