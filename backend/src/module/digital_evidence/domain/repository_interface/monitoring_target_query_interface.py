from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTargetQueryInterface(ABC):
    @abstractmethod
    async def find_active(self) -> list[MonitoringTarget]:
        pass
