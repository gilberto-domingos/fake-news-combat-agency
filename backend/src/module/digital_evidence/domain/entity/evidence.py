from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional
import hashlib
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus


class Evidence:
    def __init__(self,
                 id: UUID,
                 url: str,
                 source: str,
                 captured_at: datetime,
                 status: EvidenceStatus,
                 hash: Optional[str],
                 snapshots: Optional[list[EvidenceSnapshot]] = None,
                 ):
        self._id = id
        self._url = url
        self._source = source
        self._captured_at = captured_at
        self._status = status
        self._hash = hash
        self._snapshots = snapshots if snapshots is not None else []

    @classmethod
    def create(cls, url: str, source: str):
        captured_at = datetime.now(timezone.utc)

        hash_value = hashlib.sha256(
            f"{url}:{source}:{captured_at}".encode()
        ).hexdigest()

        return cls(
            id=uuid4(),
            url=url,
            source=source,
            captured_at=captured_at,
            status=EvidenceStatus.CAPTURED,
            hash=hash_value
        )

    @property
    def id(self) -> UUID:
        return self._id

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

    @property
    def status(self) -> EvidenceStatus:
        return self._status

    @status.setter
    def status(self, value: EvidenceStatus) -> None:
        if not isinstance(value, EvidenceStatus):
            raise ValueError("Invalid status type")
        self._status = value

    @property
    def hash(self) -> Optional[str]:
        return self._hash

    @hash.setter
    def hash(self, value: Optional[str]) -> None:
        self._hash = value

    @property
    def snapshots(self) -> list[EvidenceSnapshot]:
        return self._snapshots

    @snapshots.setter
    def snapshots(self, value: list[EvidenceSnapshot]) -> None:
        if value is None:
            raise ValueError("Snapshots cannot be None")
        self._snapshots = value

    def mark_processing(self) -> None:
        self._status = EvidenceStatus.PROCESSING

    def mark_validated(self) -> None:
        self._status = EvidenceStatus.VALIDATED

    def mark_failed(self) -> None:
        self._status = EvidenceStatus.FAILED

    def validate(self) -> bool:
        return bool(self.url and self.source)

    def __str__(self) -> str:
        return f"Evidence(id={self.id}, url={self.url}, status={self.status})"
