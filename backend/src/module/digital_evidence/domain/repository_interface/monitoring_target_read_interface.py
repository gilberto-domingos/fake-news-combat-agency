from abc import ABC, abstractmethod


class MonitoringTargetReadInterface(ABC):
    @abstractmethod
    async def find_active_keywords(self, keywords: list[str], is_active: bool) -> list[list[str]]:
        pass
