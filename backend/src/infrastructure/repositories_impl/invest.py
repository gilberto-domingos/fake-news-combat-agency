from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.invest import Invest
from src.domain.repositories_int.invest import InvestRepository
from src.infrastructure.mappers.invest_mapper import InvestMapper


class InvestRepositoryImpl(InvestRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, invest: Invest) -> None:
        model = InvestMapper.to_model(invest)
        self.session.add(model)
        await self.session.commit()
