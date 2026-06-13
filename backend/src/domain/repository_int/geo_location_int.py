from abc import abstractmethod
from typing import Protocol


class GeoLocationServiceInt(Protocol):

    @abstractmethod
    def get_city(self, ip: str) -> str | None:
        pass

    @abstractmethod
    def get_country(self, ip: str) -> str | None:
        pass
