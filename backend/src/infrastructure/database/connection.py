from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def create_engine() -> AsyncEngine:
    global _engine

    _engine = create_async_engine(
        "postgresql+asyncpg://police_user:police_pass@localhost:5432/police_db",
        echo=True,
        pool_pre_ping=True,
    )
    return _engine


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    global _session_factory

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

# FastAPI dependency
async def get_session() -> AsyncSession:
    async with get_session_factory()() as session:
        yield session

