from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Date
from uuid import uuid4
from datetime import date
from src.infrastructure.database.base import Base

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    birthdate: Mapped[date]
    gender: Mapped[str] = mapped_column(String(20))
    profession: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    password_hash: Mapped[str] = mapped_column(String(255))