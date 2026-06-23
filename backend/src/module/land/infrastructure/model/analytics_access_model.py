from uuid import UUID, uuid4
from datetime import datetime, timezone

from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.shared_infrastructure.database.base import Base


class AnalyticsAccessModel(Base):
    __tablename__ = "analytics_access"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    route: Mapped[str] = mapped_column(String(255))

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    user_agent: Mapped[str] = mapped_column(String(1000))

    language: Mapped[str] = mapped_column(String(50))

    platform: Mapped[str] = mapped_column(String(100))

    screen_width: Mapped[int] = mapped_column(Integer)

    screen_height: Mapped[int] = mapped_column(Integer)

    timezone: Mapped[str] = mapped_column(String(100))

    session_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    fingerprint: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    ip_address: Mapped[str] = mapped_column(String(100))

    country: Mapped[str] = mapped_column(String(100))

    bot_detection: Mapped[bool] = mapped_column(Boolean)

    authenticate_user_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
