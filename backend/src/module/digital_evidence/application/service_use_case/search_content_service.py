from src.module.digital_evidence.domain.repository_interface.search_content_gateway_interface import \
    SearchContentGatewayInterface


class SearchContentService:
    def __init__(self, search_content_gateway_interface: SearchContentGatewayInterface):
        self._search_content_gateway_interface = search_content_gateway_interface

    async def forward_search_engines(self, monitoring_worker_keywords: list[list[str]]) -> list[list[str]]:
        search_results = await self._search_content_gateway_interface.search_content_social_media(
            keywords=monitoring_worker_keywords
        )
        return search_results
