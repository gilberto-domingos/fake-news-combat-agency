from src.application.query.analytics_access_count_query import AnalyticsAccessCountQuery
from src.domain.repository_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt


class AnalyticsAccessCountQueryHandler:
    def __init__(self, repository: AnalyticsAccessRepositoryInt):
        self.repository = repository

    async def handle(self, query: AnalyticsAccessCountQuery) -> int:
        filters = query.model_dump()

        return await self.repository.find_count(
            filters=filters
        )
