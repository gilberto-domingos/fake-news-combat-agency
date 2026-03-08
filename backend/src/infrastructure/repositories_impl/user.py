from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.repositories_int.user import UserRepository
from sqlalchemy import select
from src.domain.entities.user import User
import bcrypt
from src.domain.repositories_int.user import PasswordHasher
from src.infrastructure.database.models.user_model import UserModel
from src.infrastructure.mappers.user_mapper import UserMapper

class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> None:
        model = UserMapper.to_model(user)
        self.session.add(model)
        await self.session.commit()

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return UserMapper.to_entity(model)

class BcryptPasswordHasher(PasswordHasher):

    def hash(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
