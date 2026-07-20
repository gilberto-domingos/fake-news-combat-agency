from uuid import UUID
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.shared_infrastructure.database.base import Base


class EvidenceSnapshotModel(Base):
    __tablename__ = "evidence_snapshots"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True
    )

    evidence_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("evidence.id"),
        nullable=False,
        index=True
    )

    evidence = relationship(
        "EvidenceModel",
        back_populates="evidence_snapshot"
    )

    text_content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    html_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    screenshot_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now
    )
