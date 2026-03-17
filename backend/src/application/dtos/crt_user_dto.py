from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import date
from typing import Literal


class CreateUserDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(min_length=2, max_length=50)
    lastname: str = Field(min_length=2, max_length=50)
    email: EmailStr
    birthdate: date
    gender: Literal["Masculino", "Feminino", "Não binário", "Transgênero", "Outro"]
    profession: str = Field(max_length=100)
    phone: str = Field(min_length=10, max_length=20)
    password: str = Field(min_length=8)
    terms_accepted: bool = Field(alias="termsAccepted")
    captcha_token: str = Field(alias="captchaToken")
