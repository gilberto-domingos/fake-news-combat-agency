from abc import ABC, abstractmethod
from uuid import UUID
from src.module.digital_evidence.domain.entity.incident import Incident


class IncidentInterface(ABC):
    @abstractmethod
    async def create(self, incident: Incident) -> Incident:
        pass

    @abstractmethod
    async def find_by_id(self, incident_id: UUID) -> Incident | None:
        pass
