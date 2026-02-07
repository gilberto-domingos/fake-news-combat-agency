from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text

from src.infrastructure.database.database import connect_db, disconnect_db
import src.infrastructure.database.database as database



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan da aplicação.

    Responsável por:
    - Conectar no banco de dados (Postgres async)
    - Inicializar cache (Redis futuramente)
    - Inicializar message broker (se houver)
    - Warm-up de modelos / serviços
    """
    print("API iniciando...")
    await connect_db()

    yield

    print("API finalizando...")
    await disconnect_db()


app = FastAPI(
    title="Police Fake News API",
    version="0.1.0",
    lifespan=lifespan,
)


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
async def health_check_db():
    """
    Health check do banco de dados.

    Valida:
    - Se o container do Postgres está acessível
    - Se a API consegue abrir conexão async
    """
    try:
        # SessionLocal só existe após connect_db()
        async with database.SessionLocal() as session:
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
