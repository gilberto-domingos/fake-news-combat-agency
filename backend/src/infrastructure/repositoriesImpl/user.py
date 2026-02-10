from sqlalchemy.ext.asyncio import AsyncSession
from domain.repositoriesCtr.user import UserRepository
from sqlalchemy import select
from domain.entities.user import User

class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> None:
        self.session.add(user)        # ORM adiciona o objeto
        await self.session.commit()   # commit assíncrono

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == str(email))
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()  # retorna um objeto User ou None
        return user
