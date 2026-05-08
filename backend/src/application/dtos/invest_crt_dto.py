from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime


class InvestCreateDto(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    proposal: str = Field(min_length=2, max_length=500)
    email: EmailStr
