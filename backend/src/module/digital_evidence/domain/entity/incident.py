from uuid import UUID, uuid4
from datetime import datetime, timezone
from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus


class Incident:
    def __init__(
            self,
            id: UUID,
            monitoring_target_id: UUID,
            title: str,
            description: str,
            status: IncidentStatus,
            created_at: datetime
    ):
        self._id = id
        self._monitoring_target_id = monitoring_target_id
        self._title = title
        self._description = description
        self._status = status
        self._created_at = created_at

    @classmethod
    def create(
            cls,
            monitoring_target_id: UUID,
            title: str,
            description: str,
    ):
        entity = cls(
            id=uuid4(),
            monitoring_target_id=monitoring_target_id,
            title=title,
            description=description,
            status=IncidentStatus.OPEN,
            created_at=datetime.now(timezone.utc),
        )
        return entity

    @classmethod
    def from_persistence(
            cls,
            id: UUID,
            monitoring_target_id: UUID,
            title: str,
            description: str,
            status: IncidentStatus,
            created_at: datetime
    ):
        persistence = cls(
            id=id,
            monitoring_target_id=monitoring_target_id,
            title=title,
            description=description,
            status=status,
            created_at=created_at
        )
        return persistence

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def monitoring_target_id(self) -> UUID:
        return self._monitoring_target_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value:
            raise ValueError("Title cannot to be empty")
        self.title = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if not value:
            raise ValueError("Description cannot to be empty")
        self._description = value

    @property
    def status(self) -> IncidentStatus:
        return self._status

    @status.setter
    def status(self, value: IncidentStatus) -> None:
        if not isinstance(value, IncidentStatus):
            raise ValueError("Invalid status type")
        self._status = value

    @property
    def created_at(self) -> datetime:
        return self._created_at
