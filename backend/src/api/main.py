from contextlib import asynccontextmanager
from fastapi import FastAPI
import os
import uvicorn
import logging

from src.api.routers.user import router as users
from src.api.middlewares.exception_handler import (
    business_exception_handler,
    validation_exception_handler,
    domain_exception_handler
)

from src.domain.exceptions.business_exception import BusinessException
from src.domain.exceptions.validation_exception import ValidationException
from src.domain.exceptions.domain_exception import DomainException

from src.infrastructure.config.cors import setup_cors


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API iniciando... (modo teste sem banco)")
    yield
    print("API finalizando...")


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


@app.get("/")
async def root():
    return {"message": "API running"}


@app.get("/healthz")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=port)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)