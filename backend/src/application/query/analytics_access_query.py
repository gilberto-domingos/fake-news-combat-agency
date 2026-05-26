from typing import Optional
from pydantic import BaseModel, Field


class AnalyticsAccessQuery(BaseModel):
    route: Optional[str] = None
    language: Optional[str] = None
    platform: Optional[str] = None
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
