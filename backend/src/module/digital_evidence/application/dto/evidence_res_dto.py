from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus


class EvidenceResDto(BaseModel):
    id: UUID
    url: str
    source: str
    captured_at: datetime
    status: EvidenceStatus
    hash: Optional[str] = None
