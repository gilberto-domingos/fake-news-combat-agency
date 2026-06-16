from src.module.land.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String
from uuid import uuid4


class InvestModel(Base):
    __tablename__ = "invests"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100))
    proposal: Mapped[str] = mapped_column(String(500))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
