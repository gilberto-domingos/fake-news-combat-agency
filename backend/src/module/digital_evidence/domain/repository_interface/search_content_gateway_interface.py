from abc import ABC, abstractmethod


class SearchContentGatewayInterface(ABC):
    @abstractmethod
    async def search_content_social_media(self, keywords: list[list[str]]):
        pass
