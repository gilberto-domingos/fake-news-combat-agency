from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MonitoringTargetResponseDto(BaseModel):
    model_config = {
        "from_attributes": True
    }

    id: UUID
    target_name: str
    keywords: list[str]
    is_active: bool
    created_at: datetime
