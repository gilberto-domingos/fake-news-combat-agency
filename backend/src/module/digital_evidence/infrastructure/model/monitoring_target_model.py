from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy.orm import relationship

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.shared_infrastructure.database.base import Base


class MonitoringTargetModel(Base):
    __tablename__ = "monitoring_target"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    incidents = relationship(
        "IncidentModel",
        back_populates="monitoring_target"
    )

    target_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    keywords: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False,
        default=list
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow
    )
