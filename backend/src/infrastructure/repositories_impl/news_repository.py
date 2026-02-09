from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text


class NewsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def count(self) -> int:
        result = await self.session.execute(
            text("SELECT COUNT(*) FROM news")
        )
        return result.scalar_one()
