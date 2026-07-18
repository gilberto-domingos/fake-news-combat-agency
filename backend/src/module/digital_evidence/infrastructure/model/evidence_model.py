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


class DigitalEvidenceModel(Base):
    __tablename__ = "digital_evidences"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True
    )

    incident_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("incidents.id"),
        nullable=False,
        index=True
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

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    hash: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    incident = relationship(
        "IncidentModel",
        back_populates="evidences"
    )

    snapshots = relationship(
        "EvidenceSnapshotModel",
        back_populates="evidence",
        cascade="all, delete-orphan"
    )
