from typing import Optional
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class AnalyticsAccessQuery(BaseModel):
    id: Optional[UUID] = None
    route: Optional[str] = None
    timestamp: Optional[datetime] = None
    user_agent: Optional[str] = None
    language: Optional[str] = None
    platform: Optional[str] = None
    screen_width: Optional[int] = None
    screen_height: Optional[int] = None
    timezone: Optional[str] = None
    sessionId: Optional[str] = None
    fingerprint: Optional[str] = None
    ip_address: Optional[str] = None
    country: Optional[str] = None
    bot_detection: Optional[bool] = None
    authenticate_user_id: Optional[str] = None

    page: int = Field(default=1, ge=1)
    limit: int = Field(default=50, ge=1, le=500)

    class Config:
        populate_by_name = True
