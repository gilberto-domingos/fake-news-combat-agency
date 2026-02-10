from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from infrastructure.database.connection import (create_engine,create_session_factory,dispose_engine)
from api.routers.user import router as users

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API iniciando...")

    engine = create_engine()
    create_session_factory(engine)

    yield

    print("API finalizando...")
    await dispose_engine(engine)

app = FastAPI(
    title="Police Fake News API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(users)