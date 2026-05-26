from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
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

        if filters.get("id"):
            query = query.where(
                AnalyticsAccessModel.id == filters["id"]
            )

        if filters.get("route"):
            query = query.where(
                AnalyticsAccessModel.route == filters["route"]
            )

        if filters.get("timestamp"):
            query = query.where(
                AnalyticsAccessModel.timestamp == filters["timestamp"]
            )

        if filters.get("user_agent"):
            query = query.where(
                AnalyticsAccessModel.user_agent == filters["user_agent"]
            )

        if filters.get("language"):
            query = query.where(
                AnalyticsAccessModel.language == filters["language"]
            )

        if filters.get("platform"):
            query = query.where(
                AnalyticsAccessModel.platform == filters["platform"]
            )

        if filters.get("screen_width"):
            query = query.where(
                AnalyticsAccessModel.screen_width == filters["screen_width"]
            )

        if filters.get("screen_height"):
            query = query.where(
                AnalyticsAccessModel.screen_height == filters["screen_height"]
            )

        if filters.get("timezone"):
            query = query.where(
                AnalyticsAccessModel.timezone == filters["timezone"]
            )

        if filters.get("sessionId"):
            query = query.where(
                AnalyticsAccessModel.session_id == filters["sessionId"]
            )

        if filters.get("fingerprint"):
            query = query.where(
                AnalyticsAccessModel.fingerprint == filters["fingerprint"]
            )

        if filters.get("ip_address"):
            query = query.where(
                AnalyticsAccessModel.ip_address == filters["ip_address"]
            )

        if filters.get("country"):
            query = query.where(
                AnalyticsAccessModel.country == filters["country"]
            )

        if filters.get("authenticate_user_id"):
            query = query.where(
                AnalyticsAccessModel.authenticate_user_id
                == filters["authenticate_user_id"]
            )

        if filters.get("bot_detection") is not None:
            query = query.where(
                AnalyticsAccessModel.bot_detection
                == filters["bot_detection"]
            )

        query = query.offset(offset).limit(limit)

        result = await self.session.execute(query)
        models = result.scalars().all()

        return [
            AnalyticsAccessMapper.to_entity(m)
            for m in models
        ]

    async def find_count(self, filters: dict) -> int:
        query = select(func.count()).select_from(AnalyticsAccessModel)

        if filters.get("id"):
            query = query.where(
                AnalyticsAccessModel.id == filters["id"]
            )

        if filters.get("route"):
            query = query.where(
                AnalyticsAccessModel.route == filters["route"]
            )

        if filters.get("timestamp"):
            query = query.where(
                AnalyticsAccessModel.timestamp == filters["timestamp"]
            )

        if filters.get("user_agent"):
            query = query.where(
                AnalyticsAccessModel.user_agent == filters["user_agent"]
            )

        if filters.get("language"):
            query = query.where(
                AnalyticsAccessModel.language == filters["language"]
            )

        if filters.get("platform"):
            query = query.where(
                AnalyticsAccessModel.platform == filters["platform"]
            )

        if filters.get("screen_width"):
            query = query.where(
                AnalyticsAccessModel.screen_width == filters["screen_width"]
            )

        if filters.get("screen_height"):
            query = query.where(
                AnalyticsAccessModel.screen_height == filters["screen_height"]
            )

        if filters.get("timezone"):
            query = query.where(
                AnalyticsAccessModel.timezone == filters["timezone"]
            )

        if filters.get("sessionId"):
            query = query.where(
                AnalyticsAccessModel.session_id == filters["sessionId"]
            )

        if filters.get("fingerprint"):
            query = query.where(
                AnalyticsAccessModel.fingerprint == filters["fingerprint"]
            )

        if filters.get("ip_address"):
            query = query.where(
                AnalyticsAccessModel.ip_address == filters["ip_address"]
            )

        if filters.get("country"):
            query = query.where(
                AnalyticsAccessModel.country == filters["country"]
            )

        if filters.get("authenticate_user_id"):
            query = query.where(
                AnalyticsAccessModel.authenticate_user_id
                == filters["authenticate_user_id"]
            )

        if filters.get("bot_detection") is not None:
            query = query.where(
                AnalyticsAccessModel.bot_detection
                == filters["bot_detection"]
            )

        result = await self.session.execute(query)

        count: int = result.scalar_one()

        return count
