from src.application.query.analytics_access_query import AnalyticsAccessQuery
from src.domain.repository_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt


class AnalyticsAccessQueryHandler:

    def __init__(self, repository: AnalyticsAccessRepositoryInt):
        self.repository = repository

    async def handle(self, query: AnalyticsAccessQuery):
        offset = (query.page - 1) * query.limit

        filters = query.model_dump(exclude={"page", "limit"})

        return await self.repository.find_all(
            filters=filters,
            limit=query.limit,
            offset=offset
        )
