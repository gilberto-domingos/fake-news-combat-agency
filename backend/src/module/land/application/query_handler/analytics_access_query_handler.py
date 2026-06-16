from src.module.land.application.query.analytics_access_query import AnalyticsAccessQuery
from src.module.land.domain.repository_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt


class AnalyticsAccessQueryHandler:

    def __init__(self, repository: AnalyticsAccessRepositoryInt):
        self.repository = repository

    async def handle(self, query: AnalyticsAccessQuery):
        LIMIT = 5

        page = max(query.page, 1)
        offset = (page - 1) * LIMIT

        filters = query.model_dump(
            exclude={"page", "limit"}
        )

        return await self.repository.find_all(
            filters=filters,
            limit=LIMIT,
            offset=offset
        )
