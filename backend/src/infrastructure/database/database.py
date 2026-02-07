from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# localhos agora porque back-end está rodando localmente
DATABASE_URL = "postgresql+asyncpg://police_user:police_pass@localhost:5432/police_db"

engine: AsyncEngine | None = None
SessionLocal: async_sessionmaker[AsyncSession] | None = None


async def connect_db() -> None:
    global engine, SessionLocal

    engine = create_async_engine(
        DATABASE_URL,
        echo=True,        # log SQL (bom em dev)
        pool_pre_ping=True,
    )

    SessionLocal = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
    )


async def disconnect_db() -> None:
    if engine:
        await engine.dispose()
