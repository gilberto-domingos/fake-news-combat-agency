from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AnalyticsAccessCrtDto(BaseModel):
    route: str
    timestamp: datetime
    city: Optional[str] = None
    user_agent: str
    language: str
    platform: str
    screen_width: int
    screen_height: int
    session_id: str = Field(alias="sessionId")
    fingerprint: str
    authenticate_user_id: Optional[str] = Field(
        default=None,
        alias="authenticate_user_id"
    )

    class Config:
        populate_by_name = True
