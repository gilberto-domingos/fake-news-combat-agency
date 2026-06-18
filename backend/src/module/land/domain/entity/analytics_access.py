from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime
from typing import Optional


class AnalyticsAccess(ABC):
    def __init__(
            self,
            id: UUID,
            route: str,
            timestamp: datetime,
            user_agent: str,
            language: str,
            platform: str,
            screen_width: int,
            screen_height: int,
            timezone: str,
            ip_address: str,
            country: str,
            bot_detection: bool,
            city: Optional[str] = None,
            session_id: Optional[str] = None,
            fingerprint: str = "",
            authenticate_user_id: Optional[str] = None,
    ):
        self._id = id
        self._route = route
        self._timestamp = timestamp
        self._city = city
        self._user_agent = user_agent
        self._language = language
        self._platform = platform
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._timezone = timezone
        self._session_id = session_id
        self._fingerprint = fingerprint
        self._ip_address = ip_address
        self._country = country
        self._bot_detection = bot_detection
        self._authenticate_user_id = authenticate_user_id

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def route(self) -> str:
        return self._route

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def city(self) -> Optional[str]:
        return self._city

    @city.setter
    def city(self, value: Optional[str]) -> None:
        self._city = value

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @property
    def language(self) -> str:
        return self._language

    @property
    def platform(self) -> str:
        return self._platform

    @property
    def screen_width(self) -> int:
        return self._screen_width

    @property
    def screen_height(self) -> int:
        return self._screen_height

    @property
    def timezone(self) -> str:
        return self._timezone

    @property
    def session_id(self) -> Optional[str]:
        return self._session_id

    @property
    def fingerprint(self) -> str:
        return self._fingerprint

    @property
    def ip_address(self) -> str:
        return self._ip_address

    @property
    def country(self) -> str:
        return self._country

    @property
    def bot_detection(self) -> bool:
        return self._bot_detection

    @property
    def authenticate_user_id(self) -> Optional[str]:
        return self._authenticate_user_id

    @authenticate_user_id.setter
    def authenticate_user_id(self, value: Optional[str]) -> None:
        self._authenticate_user_id = value

    def is_bot(self) -> bool:
        return self._bot_detection is True

    def is_authenticated(self) -> bool:
        return self._authenticate_user_id is not None

    def __str__(self) -> str:
        return f"AnalyticsAccess(id={self.id}, route={self.route}, country={self.country})"

    @abstractmethod
    def validate(self) -> bool:
        pass
