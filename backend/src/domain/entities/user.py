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

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        if not value:
            raise ValueError("Lastname cannot be empty")
        self._lastname = value

    @property
    def email(self) -> Email:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not value:
            raise ValueError("Email cannot be empty")
        self._email = value

    @property
    def birthdate(self) -> date:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value: str) -> None:
        if not value:
            raise ValueError("Birthdate cannot be empty")
        self._birthdate = value

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, value: str) -> None:
        if not value:
            raise ValueError("Gender cannot be empty")
        self._gender = value

    @property
    def profession(self) -> str:
        return self._profession

    @profession.setter
    def profession(self, value: str) -> None:
        if not value:
            raise ValueError("Profession cannot be empty")
        self._profession = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        if not value:
            raise ValueError("Phone be empty")
        self._phone = value

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str) -> None:
        if not value:
            raise ValueError(" Password cannot be empty")
        self._password_hash = value

    @property
    def terms_accepted(self) -> bool:
        return self._terms_accepted

    @terms_accepted.setter
    def terms_accepted(self, value: str) -> None:
        if not value:
            raise ValueError("Terms cannot be empty")
        self._terms_accepted = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def __str__(self):
        return f"User=(user={self.name}, lastname={selt.lastname}, email={self.email}, birthdate={self.birthdate}, gender={self.gender}, profession={self.profession}, phone={self.phone}, passwor_hash={self.password_hash}, terms_accepted={self.terms_accepted}, created_at={self.created_at})"
