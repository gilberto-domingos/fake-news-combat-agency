from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.incident import Incident


class IncidentWriteInterface(ABC):
    @abstractmethod
    async def create(self, incident: Incident) -> Incident:
        pass
