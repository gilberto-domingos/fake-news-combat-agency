from uuid import UUID, uuid4
from datetime import datetime, timezone

from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus
from src.module.digital_evidence.domain.exception.business_exception import BusinessException


class Evidence:
    def __init__(
            self,
            id: UUID,
            incident_id: UUID,
            url: str,
            source: str,
            captured_at: datetime,
            status: EvidenceStatus,
            hash: str
    ):
        self._id = id
        self._incident_id = incident_id
        self._url = url
        self._source = source
        self._captured_at = captured_at
        self._status = status
        self._hash = hash

    @classmethod
    def create(
            cls,
            incident_id: UUID,
            url: str,
            source: str,
            hash: str
    ):
        entity = cls(
            id=uuid4(),
            incident_id=incident_id,
            url=url,
            source=source,
            captured_at=datetime.now(timezone.utc),
            status=EvidenceStatus.PROCESSING,
            hash=hash
        )
        return entity

    @classmethod
    def from_persistence(
            cls,
            id: UUID,
            incident_id: UUID,
            url: str,
            source: str,
            captured_at: datetime,
            status: EvidenceStatus,
            hash: str,
    ):
        persistence = cls(
            id=id,
            incident_id=incident_id,
            url=url,
            source=source,
            captured_at=captured_at,
            status=status,
            hash=hash,
        )
        return persistence

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def incident_id(self) -> UUID:
        return self._incident_id

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        if not value:
            raise ValueError("URL cannot be empty")
        self._url = value

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value: str) -> None:
        if not value:
            raise ValueError("Source cannot be empty")
        self._source = value

    @property
    def captured_at(self) -> datetime:
        return self._captured_at

    @captured_at.setter
    def captured_at(self, value: datetime):
        self._captured_at = value

    @property
    def status(self) -> EvidenceStatus:
        return self._status

    @status.setter
    def status(self, value: EvidenceStatus) -> None:
        if not isinstance(value, EvidenceStatus):
            raise ValueError("Invalid status type")
        self._status = value

    @property
    def hash(self) -> str:
        return self._hash

    def mark_processing(self) -> None:
        self._status = EvidenceStatus.PROCESSING
        self._captured_at = datetime.now(timezone.utc)

    def mark_validated(self) -> None:
        if self._status is EvidenceStatus.FAILED:
            raise BusinessException(
                message="Failed evidence cannot be validated",
                error_code="FAILED_EVIDENCE_CANNOT_BE_VALIDATED"
            )
        self._status = EvidenceStatus.VALIDATED

    def mark_failed(self) -> None:
        self._status = EvidenceStatus.FAILED

    def __str__(self) -> str:
        return (
            f"Evidence(id={self.id}, incident_id={self.incident_id}, "
            f"url={self.url}, source={self.source}, "
            f"captured_at={self.captured_at}, status={self.status}, "
            f"hash={self.hash})"
        )
