from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus


class IncidentResponseDto(BaseModel):
    model_config = {
        "from_attributes": True
    }

    id: UUID
    monitoring_target_id: UUID
    title: str
    description: str
    status: IncidentStatus
    created_at: datetime
