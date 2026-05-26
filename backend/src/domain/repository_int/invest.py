from abc import ABC, abstractmethod
from src.domain.entity.invest import Invest


class InvestRepository(ABC):
    @abstractmethod
    async def save(self, invest: Invest) -> None:
        pass
