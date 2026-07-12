from uuid import UUID, uuid4
from datetime import datetime


class MonitoringTarget:
    def __init__(self,
                 id: UUID,
                 target_name: str,
                 keywords: list[str],
                 is_active: bool,
                 created_at: datetime):
        self._id = id
        self._target_name = target_name
        self._keywords = keywords
        self._is_active = is_active
        self._created_at = created_at

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def target_name(self) -> str:
        return self._target_name

    @target_name.setter
    def target_name(self, value: str) -> None:
        if not value:
            raise ValueError("Target name cannot to be empty")
        self._target_name = value

    @property
    def keywords(self) -> list[str]:
        return self._keywords

    @keywords.setter
    def keywords(self, value: list[str]) -> None:
        self._keywords = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool) -> None:
        self._is_active = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def activate(self) -> None:
        if self._is_active:
            raise ValueError("Target is already is active")
        self._is_active = True

    def deactivate(self) -> None:
        if not self._is_active:
            raise ValueError("Target is already is deactivate")
        self._is_active = False

    def add_keywords(self, keywords: list[str]) -> None:
        self._keywords.extend(keywords)

    def update_keywords(self, keywords: list[str]) -> None:
        self._keywords = keywords
