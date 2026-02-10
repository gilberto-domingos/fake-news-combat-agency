from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4
from domain.valueObjects.email import Email

Base = declarative_base()  # base para ORM

class User(Base):
    __tablename__ = "users"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, username: str, email: Email, password: str, user_id=None):
        self.id = user_id or uuid4()
        self.username = username
        self.email = str(email)  # armazenamos o value object como string no banco
        self.password = password
        self.created_at = datetime.utcnow()
