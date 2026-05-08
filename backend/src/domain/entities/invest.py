from datetime import datetime, date, timezone
from uuid import UUID, uuid4
from src.domain.value_objects.email import Email


class Invest:
    def __init__(self, name: str, proposal: str, email: Email, id: UUID | None = None,
                 created_at: datetime | None = None):
        self._id = id or uuid4()
        self._name = name
        self._proposal = proposal
        self._email = email
        self._created_at = created_at or datetime.now(timezone.utc)

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def proposal(self) -> str:
        return self._proposal

    @proposal.setter
    def proposal(self, value: str) -> None:
        if not value:
            raise ValueError("Proposal cannot be empty")
        self._proposal = value

    @property
    def email(self) -> Email:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not value:
            raise ValueError("Email cannot be empty")
        self._email = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def __str__(self):
        return f"Invest=(invest={self.name}, proposal={self.proposal}, email={self.email}, created_at={self.created_at})"
