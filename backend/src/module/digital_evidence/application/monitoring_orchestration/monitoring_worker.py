from src.module.digital_evidence.domain.repository_interface.monitoring_target_read_interface import \
    MonitoringTargetReadInterface
from src.module.digital_evidence.application.service_use_case.search_content_service import SearchContentService


class MonitoringWorker():
    def __init__(self, repository: MonitoringTargetReadInterface, search_content_service: SearchContentService):
        self._repository = repository
        self._search_content_service = search_content_service

    async def execute(self, keywords: list[str], is_active: bool) -> list[list[str]]:
        get_values = await self._repository.find_active_keywords(
            keywords=keywords,
            is_active=is_active,
        )

        search_results = await self._search_content_service.forward_search_engines(
            monitoring_worker_keywords=get_values,
        )

        return search_results
