from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class AnalyticsAccessCreateCommand(BaseModel):
    route: str
    timestamp: datetime
    city: str
    user_agent: str
    language: str
    platform: str
    screen_width: int
    screen_height: int
    timezone: str
    sessionId: str
    fingerprint: str
    authenticate_user_id: Optional[str] = None

    class Config:
        populate_by_name = True


@dataclass
class RequestMetadata:
    ip_address: str
    country: str
    bot_detection: bool
