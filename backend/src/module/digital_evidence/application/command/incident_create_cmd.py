from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class IncidentCreateCommand:
    monitoring_target_id: UUID
    title: str
    description: str
