from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus


class IncidentResDto(BaseModel):
    id: UUID
    monitoring_target_id: UUID
    title: str
    description: str
    status: IncidentStatus
    created_at: datetime
