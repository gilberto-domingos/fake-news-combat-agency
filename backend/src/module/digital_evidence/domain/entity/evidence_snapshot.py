from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from typing import Optional


class EvidenceSnapshot(ABC):
    def __init__(self, evidence_id: UUID, html_content: str, screenshot_path: str, hash: Optional[str],
                 text_content: str):
        self._id: UUID = uuid4()
        self._evidence_id = evidence_id
        self._html_content = html_content
        self._screenshot_path = screenshot_path
        self._hash = hash
        self._text_content = text_content

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def evidence_id(self) -> UUID:
        return self._evidence_id

    @property
    def html_content(self) -> str:
        return self._html_content

    @html_content.setter
    def html_content(self, value: str) -> None:
        if not value:
            raise ValueError("HTML content cannot be empty")
        self._html_content = value

    @property
    def screenshot_path(self) -> str:
        return self._screenshot_path

    @screenshot_path.setter
    def screenshot_path(self, value: str) -> None:
        if not value:
            raise ValueError("Screenshot path cannot be empty")
        self._screenshot_path = value

    @property
    def hash(self) -> Optional[str]:
        return self._hash

    @hash.setter
    def hash(self, value: str) -> None:
        self.hash = value

    @property
    def text_content(self) -> str:
        return self._text_content

    @text_content.setter
    def text_content(self, value: str) -> None:
        if not value:
            raise ValueError("Text content cannot be empty")
        self._text_content = value

    def update_text_from_html(self) -> None:

        if not self._html_content:
            raise ValueError("HTML content is required to extract text")

        self._text_content = self._html_content

    @abstractmethod
    def validate(self) -> bool:
        pass

    def __str__(self) -> str:
        return f"EvidenceSnapshot(id={self.id}, evidence_id={self.evidence_id})"
