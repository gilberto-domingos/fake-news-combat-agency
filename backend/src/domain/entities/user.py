from datetime import datetime, date, timezone
from uuid import UUID, uuid4
from src.domain.value_objects.email import Email


class User:
    def __init__(self, name: str, lastname: str, email: Email, birthdate: date, gender: str, profession: str,
                 phone: str, password_hash: str, terms_accepted: bool, id: UUID | None = None,
                 created_at: datetime | None = None):
        self._id = id or uuid4()
        self._name = name
        self._lastname = lastname
        self._email = email
        self._birthdate = birthdate
        self._gender = gender
        self._profession = profession
        self._phone = phone
        self._password_hash = password_hash
        self._terms_accepted = terms_accepted
        self._created_at = created_at or datetime.now(timezone.utc)

    #   self._validate_business_rules()
    #
    # def _validate_business_rules(self):
    #     age = (date.today() - self.birthdate).days // 365
    #     if age < self.MIN_AGE:
    #         raise ValueError(f"Usuário deve ter pelo menos {self.MIN_AGE} anos")

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def lastname(self) -> str:
        return self._lastname

    @property
    def email(self) -> Email:
        return self._email

    @property
    def birthdate(self) -> date:
        return self._birthdate

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def profession(self) -> str:
        return self._profession

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @property
    def terms_accepted(self) -> bool:
        return self._terms_accepted

    @property
    def created_at(self) -> datetime:
        return self._created_at
