from pydantic import BaseModel
from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from datetime import datetime


class AnalyticsAccess(BaseModel):
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
