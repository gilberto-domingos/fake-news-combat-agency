from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus
from src.module.digital_evidence.domain.entity.incident import Incident


class Evidence:
    def __init__(self,
                 id: UUID,
                 incident: Incident,
                 url: str,
                 source: str,
                 created_at: datetime,
                 status: EvidenceStatus,
                 hash: str,
                 snapshots: Optional[list[EvidenceSnapshot]] = None,
                 ):
        self._id = id
        self._incident = incident
        self._url = url
        self._source = source
        self._created_at = created_at
        self._status = status
        self._hash = hash
        self._snapshots = snapshots if snapshots is not None else []

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def incident(self):
        return self._incident

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
    def created_at(self) -> datetime:
        return self._created_at

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

    @property
    def snapshots(self) -> list[EvidenceSnapshot]:
        return self._snapshots

    @snapshots.setter
    def snapshots(self, value: list[EvidenceSnapshot]) -> None:
        if value is None:
            raise ValueError("Snapshots cannot be None")
        self._snapshots = value

    def register_snapshot(self, snapshots: EvidenceSnapshot) -> None:
        if snapshots is None:
            raise ValueError("Snapshots cannot be none")
        if snapshots.id != self._id:
            raise ValueError("Snapshot does not belong to this evidence")
        self._snapshots.append(snapshots)

    def mark_processing(self) -> None:
        self._status = EvidenceStatus.PROCESSING

    def mark_validated(self) -> None:
        self._status = EvidenceStatus.VALIDATED

    def mark_failed(self) -> None:
        self._status = EvidenceStatus.FAILED

    def __str__(self) -> str:
        return f"Evidence(id={self.id}, url={self.url}, source={self.source},captured_at={self.captured_at}, status={self.status}, hash={self.hash}, snapshots={self.snapshots} )"
