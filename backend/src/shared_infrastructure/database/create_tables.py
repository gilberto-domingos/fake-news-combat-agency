import asyncio
from src.shared_infrastructure.database.base import Base
from src.shared_infrastructure.database.connection import create_engine
import src.shared_infrastructure.database.model_registry


async def create_tables():
    engine = create_engine()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("TABLES CREATED SUCCESSFULLY !")


if __name__ == "__main__":
    asyncio.run(create_tables())
