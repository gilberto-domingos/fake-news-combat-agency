from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTargetRepInt(ABC):
    @abstractmethod
    async def create(self, monitoring_target: MonitoringTarget) -> MonitoringTarget:
        pass
