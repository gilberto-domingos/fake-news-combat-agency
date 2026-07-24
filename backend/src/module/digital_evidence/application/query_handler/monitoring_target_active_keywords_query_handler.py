from src.module.digital_evidence.application.service_use_case.monitoring_target_find_active_keywords_service import \
    MonitoringTargetFindActiveKeywordsService
from src.module.digital_evidence.application.query.monitoring_target_active_keywords_query import \
    MonitoringTargetActiveKeywordsQuery


class MonitoringTargetActiveKeywordsQueryHandler:
    def __init__(self, service: MonitoringTargetFindActiveKeywordsService):
        self._service = service

    async def handle(self, query: MonitoringTargetActiveKeywordsQuery) -> list[list[str]]:
        result = await self._service.execute(
            keywords=query.keywords,
            is_active=query.is_active
        )

        return result
