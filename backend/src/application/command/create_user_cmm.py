from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CreateUserCommand:
    name: str
    lastname: str
    email: str
    password: str
    birthdate: date
    gender: str
    profession: str
    phone: str
    recaptcha: str
