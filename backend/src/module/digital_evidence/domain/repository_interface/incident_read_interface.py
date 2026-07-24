from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.incident import Incident
from uuid import UUID


class IncidentReadInterface(ABC):
    @abstractmethod
    async def find_by_id(self, incident_id: UUID) -> Incident | None:
        pass
