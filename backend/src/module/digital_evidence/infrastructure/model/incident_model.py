from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus
from src.shared_infrastructure.database.base import Base
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship


class IncidentModel(Base):
    __tablename__ = "incident"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    monitoring_target_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("monitoring_target.id"),
        nullable=False
    )

    monitoring_target = relationship(
        "MonitoringTargetModel",
        back_populates="incident"
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    status: Mapped[IncidentStatus] = mapped_column(
        SQLEnum(IncidentStatus),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now
    )
