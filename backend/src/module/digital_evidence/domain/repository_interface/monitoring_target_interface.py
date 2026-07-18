from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget
from uuid import UUID


class MonitoringTargetInterface(ABC):
    @abstractmethod
    async def create(self, monitoring_target: MonitoringTarget) -> MonitoringTarget:
        pass

    @abstractmethod
    async def find_by_id(self, monitoring_target_id: UUID) -> MonitoringTarget | None:
        pass

    """
    @abstractmethod
    async def update(self, monitoring_target: MonitoringTarget) -> None:
        pass

    @abstractmethod
    async def delete(self, monitoring_target_id: UUID) -> None:
        pass
"""
