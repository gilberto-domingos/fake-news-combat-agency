from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.domain.entity.analytics_access import AnalyticsAccess
from src.domain.repository_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt
from src.infrastructure.mapper.analytics_access_mapper import AnalyticsAccessMapper
from src.infrastructure.database.model.analytics_access_model import AnalyticsAccessModel


class AnalyticsAccessRepositoryImpl(AnalyticsAccessRepositoryInt):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, analytics_access: AnalyticsAccess) -> AnalyticsAccess:
        model = AnalyticsAccessMapper.to_model(analytics_access)

        self.session.add(model)

        await self.session.commit()
        await self.session.refresh(model)

        return AnalyticsAccessMapper.to_entity(model)

    async def find_all(self, filters: dict, limit: int, offset: int) -> list[AnalyticsAccess]:
        query = select(AnalyticsAccessModel)

        if filters.get("route"):
            query = query.where(AnalyticsAccessModel.route == filters["route"])

        if filters.get("country"):
            query = query.where(AnalyticsAccessModel.country == filters["country"])

        if filters.get("ip_address"):
            query = query.where(AnalyticsAccessModel.ip_address == filters["ip_address"])

        if filters.get("authenticate_user_id"):
            query = query.where(
                AnalyticsAccessModel.authenticate_user_id
                == filters["authenticate_user_id"]
            )

        if filters.get("bot_detection") is not None:
            query = query.where(
                AnalyticsAccessModel.bot_detection == filters["bot_detection"]
            )

        query = query.offset(offset).limit(limit)

        result = await self.session.execute(query)
        models = result.scalars().all()

        return [
            AnalyticsAccessMapper.to_entity(m)
            for m in models
        ]
