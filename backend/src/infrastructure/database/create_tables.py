import asyncio
from src.infrastructure.database.base import Base
from src.infrastructure.database.connection import create_engine
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


async def create_tables():
    engine = create_engine()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    print("TABLES CREATED SUCCESSFULLY !")


if __name__ == "__main__":
    asyncio.run(create_tables())
