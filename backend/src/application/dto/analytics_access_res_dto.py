from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class AnalyticsAccessResDto(BaseModel):
    id: UUID
    route: str
    timestamp: datetime
    user_agent: str
    language: str
    platform: str
    screen_width: int
    screen_height: int
    timezone: str
    sessionId: str
    fingerprint: str
    ip_address: str
    country: str
    bot_detection: bool
    authenticate_user_id: Optional[str] = None
