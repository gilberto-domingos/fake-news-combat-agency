from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, username: str, email: str, password: str) -> User:
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError("Email already registered")

        user = User(username=username, email=email, password=password)
        await self.user_repository.save(user)
        return user
