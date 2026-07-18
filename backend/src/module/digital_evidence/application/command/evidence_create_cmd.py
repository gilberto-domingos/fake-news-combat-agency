from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class EvidenceCreateCommand:
    incident_id: UUID
    url: str
    source: str
    hash: str
