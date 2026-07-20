from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus


class IncidentCreateDtoExperiment(BaseModel):
    monitoring_target_id: UUID
    title: str
    description: str
    status: IncidentStatus
    created_at: datetime
