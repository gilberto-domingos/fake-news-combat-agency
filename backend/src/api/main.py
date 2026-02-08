from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from infrastructure.database.connection import (
    create_engine,
    create_session_factory,
    dispose_engine,
)



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan da aplicação.

    Responsável por:
    - Criar engine async do Postgres
    - Criar session factory
    - Guardar recursos em app.state
    - Encerrar tudo corretamente no shutdown
    """
    print("API iniciando...")

    # --- Database ---
    engine: AsyncEngine = create_engine()
    session_factory: async_sessionmaker = create_session_factory(engine)

    app.state.db_engine = engine
    app.state.db_session_factory = session_factory

    yield

    print("API finalizando...")

    await dispose_engine(engine)


app = FastAPI(
    title="Police Fake News API",
    version="0.1.0",
    lifespan=lifespan,
)


# --------------------------------------------------
# Health checks
# --------------------------------------------------

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check básico.

    Usado para:
    - Docker
    - Kubernetes
    - Load Balancer
    - Monitoramento
    """
    return {"status": "ok"}


@app.get("/health/db", tags=["Health"])
async def health_check_db(request: Request):
    """
    Health check do banco de dados.

    Valida:
    - Se o Postgres está acessível
    - Se a aplicação consegue executar query async
    """
    try:
        session_factory = request.app.state.db_session_factory

        async with session_factory() as session:
            await session.execute(text("SELECT 1"))

        return {"database": "ok"}

    except Exception as exc:
        return JSONResponse(
            status_code=500,
            content={
                "database": "error",
                "detail": str(exc),
            },
        )
