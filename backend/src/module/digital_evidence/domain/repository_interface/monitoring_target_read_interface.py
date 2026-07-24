from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTargetReadInterface(ABC):
    @abstractmethod
    async def find_active_keywords(self, keywords: list[str], is_active: bool) -> list[list[str]]:
        pass
