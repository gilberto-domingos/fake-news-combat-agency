from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entity.analytics_access import AnalyticsAccess
from src.domain.repository_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt
from src.infrastructure.mapper.analytics_access_mapper import AnalyticsAccessMapper


class AnalyticsAccessRepositoryImpl(AnalyticsAccessRepositoryInt):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, analytics_access: AnalyticsAccess) -> AnalyticsAccess:
        model = AnalyticsAccessMapper.to_model(analytics_access)

        self.session.add(model)

        await self.session.commit()
        await self.session.refresh(model)

        return AnalyticsAccessMapper.to_entity(model)

        # async def find_all(self):
    #     pass
