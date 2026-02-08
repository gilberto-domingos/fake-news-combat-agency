from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

#Em produção isso vem de settings/env
DATABASE_URL = "postgresql+asyncpg://police_user:police_pass@localhost:5432/police_db"


def create_engine() -> AsyncEngine:
    """
    Cria o engine async do SQLAlchemy.

    Não guarda estado.
    Não abre conexão imediatamente.
    Apenas descreve como conectar.
    """
    return create_async_engine(
        DATABASE_URL,
        echo=True,          # bom para DEV (false em prod)
        pool_pre_ping=True,
    )


def create_session_factory(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    """
    Cria a factory de sessões async.

    Cada chamada da factory cria uma nova AsyncSession,
    reutilizando o pool de conexões do engine.
    """
    return async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
    )


async def dispose_engine(engine: AsyncEngine) -> None:
    """
    Encerra corretamente o engine e o pool de conexões.
    Usado no shutdown da aplicação.
    """
    await engine.dispose()
