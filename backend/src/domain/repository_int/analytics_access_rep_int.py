from abc import ABC, abstractmethod
from src.domain.entity.analytics_access import AnalyticsAccess


class AnalyticsAccessRepositoryInt(ABC):
    @abstractmethod
    async def create(self, analytics: AnalyticsAccess) -> AnalyticsAccess:
        pass

    # @abstractmethod
    # async def find_all(self):
    #     pass
