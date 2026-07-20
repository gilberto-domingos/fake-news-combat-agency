from uuid import UUID
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum as SQLEnum

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.shared_infrastructure.database.base import Base
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus


class EvidenceModel(Base):
    __tablename__ = "evidence"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True
    )

    incident_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("incident.id"),
        nullable=False,
        index=True
    )

    incident = relationship(
        "IncidentModel",
        back_populates="incident"
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[EvidenceStatus] = mapped_column(
        SQLEnum(EvidenceStatus),
        nullable=False,
        index=True
    )

    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now
    )

    hash: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )
