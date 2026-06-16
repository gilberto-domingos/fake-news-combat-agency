from abc import ABC, abstractmethod
from src.module.land.domain.entity.analytics_access import AnalyticsAccess


class AnalyticsAccessRepositoryInt(ABC):
    @abstractmethod
    async def create(self, analytics: AnalyticsAccess) -> AnalyticsAccess:
        pass

    @abstractmethod
    async def find_all(self, filters: dict, limit: int, offset: int) -> list[AnalyticsAccess]:
        pass

    @abstractmethod
    async def find_count(self, filters: dict) -> int:
        pass
