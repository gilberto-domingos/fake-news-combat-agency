from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
import re

class User:
    def __init__(self, username: str, email: str, password: str, user_id: Optional[UUID] = None):
        self._id = user_id or uuid4()
        self.username = username
        self.email = email
        self.password = password
        self._created_at = datetime.utcnow()

    # Encapsulamento de atributos
    @property
    def id(self) -> UUID:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if not value or len(value) < 3:
            raise ValueError("Username must have at least 3 characters")
        self._username = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        # validação simples de email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email address")
        self._email = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        if not value or len(value) < 6:
            raise ValueError("Password must have at least 6 characters")
        self._password = value
