from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID


class InvestResponseDto(BaseModel):
    id: UUID
    name: str
    proposal: str
    email: EmailStr
    created_at: datetime
