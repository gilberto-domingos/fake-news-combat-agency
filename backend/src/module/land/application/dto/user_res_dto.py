from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from uuid import UUID


class ResponseUserDto(BaseModel):
    id: UUID
    name: str
    lastname: str
    email: EmailStr
    birthdate: date
    gender: str
    profession: str
    phone: str
    terms_accepted: bool
    created_at: datetime
