from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Literal

class CreateUserDto(BaseModel):
    name: constr(min_length=2, max_length=50)
    lastname: constr(min_length=2, max_length=50)
    email: EmailStr
    password: constr(min_length=8)
    birthdate: date
    gender: Literal["Masculino", "Feminino", "Não binário", "Transgênero","Outro"]
    profession: constr(max_length=100)
    phone: constr(min_length=10, max_length=20)
    recaptcha: str