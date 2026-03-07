from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.routers.user import router as users
from api.middlewares.exception_handler import (business_exception_handler, validation_exception_handler, domain_exception_handler)
from domain.exceptions.business_exception import BusinessException
from domain.exceptions.validation_exception import ValidationException
from domain.exceptions.domain_exception import DomainException
from infrastructure.database.connection import (create_engine, create_session_factory, dispose_engine)
from infrastructure.config.cors import setup_cors
import os
import uvicorn

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

setup_cors(app)

app.include_router(users)

app.add_exception_handler(BusinessException, business_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)
app.add_exception_handler(DomainException, domain_exception_handler)

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=port)