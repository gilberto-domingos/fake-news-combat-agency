from uuid import UUID, uuid4
from typing import Optional
from hashlib import sha256


class EvidenceSnapshot:
    def __init__(self,
                 id: UUID,
                 screenshot_path: str,
                 hash: Optional[str],
                 text_content: str,
                 html_path: str):
        self._id = id
        self._screenshot_path = screenshot_path
        self._hash = hash
        self._text_content = text_content
        self._html_path = html_path

    @property
    def id(self) -> UUID:
        return self._id

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

    @property
    def html_path(self) -> str:
        return self._html_path

    @html_path.setter
    def html_path(self, value: str) -> None:
        if not value:
            raise ValueError("Html path cannot to be empty")
        self._html_path = value

    def update_text_from_html(self) -> None:
        if not self._text_content:
            raise ValueError("HTML content is required to extract text")
        self._text_content = self._text_content

    def generate_hash(self) -> None:
        content = (
            f"{self._text_content}"
            f"{self._html_path}"
            f"{self._screenshot_path}"
        )

        self._hash = sha256(
            content.encode("utf-8")
        ).hexdigest()

    def calculate_hash(self) -> str:
        content = (
            f"{self._text_content}"
            f"{self._html_path}"
            f"{self._screenshot_path}"
        )

        return sha256(
            content.encode("utf-8")
        ).hexdigest()

    def validate_integrity(self) -> bool:
        return self.calculate_hash() == self._hash

    def __str__(self) -> str:
        return f"EvidenceSnapshot(id={self.id}, screenshot_path={self.screenshot_path}, hash={self.hash}, text_content={self.text_content}, html_path={self.html_path} )"

    def __repr__(self) -> str:
        return self.__str__()
