from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class IncidentCrtCommand:
    monitoring_target_id: UUID
    title: str
    description: str
