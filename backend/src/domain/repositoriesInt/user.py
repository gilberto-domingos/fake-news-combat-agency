from abc import ABC, abstractmethod
from domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        pass

class PasswordHasher(ABC):

    @abstractmethod
    def hash(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, password: str, hashed_password: str) -> bool:
        pass