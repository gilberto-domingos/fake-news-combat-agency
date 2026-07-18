from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MonitoringTargetResponseDto(BaseModel):
    id: UUID
    target_name: str
    keywords: list[str]
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
