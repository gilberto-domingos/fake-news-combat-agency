import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# dotenv_path = Path(__file__).parent / ".env"
# load_dotenv(dotenv_path=dotenv_path)
load_dotenv()

DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def create_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        _engine = create_async_engine(
            DATABASE_URL,
            echo=True,
            pool_pre_ping=True,
        )
    return _engine


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            bind=engine,
            expire_on_commit=False,
        )
    return _session_factory


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    if _session_factory is None:
        raise RuntimeError("Session factory not initialized")
    return _session_factory


async def dispose_engine(engine: AsyncEngine) -> None:
    await engine.dispose()


async def get_session() -> AsyncSession:
    async with get_session_factory()() as session:
        yield session