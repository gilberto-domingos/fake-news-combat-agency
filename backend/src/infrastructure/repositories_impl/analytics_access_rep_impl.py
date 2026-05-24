from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.analytics_access import AnalyticsAccess
from src.domain.repositories_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt
from src.infrastructure.mappers.analytics_access_mapper import AnalyticsAccessMapper


class AnalyticsAccessRepositoryImpl(AnalyticsAccessRepositoryInt):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, analytics_access: AnalyticsAccess) -> None:
        model = AnalyticsAccessMapper.to_model(analytics_access)

        self.session.add(model)

        await self.session.commit()

    # async def find_all(self):
    #     pass
