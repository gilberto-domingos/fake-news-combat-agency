from typing import Optional
from pydantic import BaseModel, Field


class AnalyticsAccessCountQuery(BaseModel):
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
