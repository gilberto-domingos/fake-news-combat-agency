from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID


class AnalyticsAccessResDto(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )

    id: UUID

    session_id: Optional[str] = Field(
        default=None,
        alias="sessionId"
    )

    route: str
    timestamp: datetime
    user_agent: str
    language: str
    platform: str
    screen_width: int
    screen_height: int
    timezone: str
    fingerprint: str
    ip_address: str
    country: str
    bot_detection: bool
    authenticate_user_id: Optional[str] = None
