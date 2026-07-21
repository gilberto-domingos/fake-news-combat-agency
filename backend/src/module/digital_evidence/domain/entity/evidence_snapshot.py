from uuid import UUID, uuid4
from hashlib import sha256
from datetime import datetime, timezone


class EvidenceSnapshot:
    def __init__(
            self,
            id: UUID,
            evidence_id: UUID,
            text_content: str,
            html_path: str,
            screenshot_path: str,
            hash: str,
            captured_at: datetime
    ):
        self._id = id
        self._evidence_id = evidence_id
        self._text_content = text_content
        self._html_path = html_path
        self._screenshot_path = screenshot_path
        self._hash = hash
        self._captured_at = captured_at

    @classmethod
    def create(
            cls,
            evidence_id: UUID,
            text_content: str,
            html_path: str,
            screenshot_path: str,
            hash: str,
    ):
        entity = cls(
            id=uuid4(),
            evidence_id=evidence_id,
            text_content=text_content,
            html_path=html_path,
            screenshot_path=screenshot_path,
            hash=hash,
            captured_at=datetime.now(timezone.utc)
        )
        return entity

    @classmethod
    def from_persistence(
            cls,
            id: UUID,
            evidence_id: UUID,
            text_content: str,
            html_path: str,
            screenshot_path: str,
            hash: str,
            captured_at: datetime
    ):
        persistence = cls(
            id=id,
            evidence_id=evidence_id,
            text_content=text_content,
            html_path=html_path,
            screenshot_path=screenshot_path,
            hash=hash,
            captured_at=captured_at
        )
        return persistence

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def evidence_id(self) -> UUID:
        return self._evidence_id

    @property
    def screenshot_path(self) -> str:
        return self._screenshot_path

    @screenshot_path.setter
    def screenshot_path(self, value: str) -> None:
        if not value:
            raise ValueError("Screenshot path cannot be empty")
        self._screenshot_path = value

    @property
    def hash(self) -> str:
        return self._hash

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
            raise ValueError("Html path cannot be empty")
        self._html_path = value

    @property
    def captured_at(self) -> datetime:
        return self._captured_at

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
        return (
            f"EvidenceSnapshot("
            f"id={self.id}, "
            f"evidence_id={self.evidence_id}, "
            f"screenshot_path={self.screenshot_path}, "
            f"hash={self.hash})"
        )

    def __repr__(self) -> str:
        return self.__str__()
