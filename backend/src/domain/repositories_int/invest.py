from abc import ABC, abstractmethod
from src.domain.entities.invest import Invest


class InvestRepository(ABC):
    @abstractmethod
    async def save(self, invest: Invest) -> None:
        pass
