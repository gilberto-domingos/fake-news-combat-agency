from uuid import UUID
from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.module.digital_evidence.infrastructure.database.base import Base


class DigitalEvidenceModel(Base):
    __tablename__ = "evidences"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True
    )

    url: Mapped[str] = mapped_column(String(1000), nullable=False)

    source: Mapped[str] = mapped_column(String(100), nullable=False)

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )

    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    hash: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )
