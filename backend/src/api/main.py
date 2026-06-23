import logging
import os
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.api.router_registry_global import api_router
from src.api.exception_handler.exception_registry import register_exception_handlers
from src.shared_infrastructure.config.cors import setup_cors
from src.shared_infrastructure.database.connection import (
    create_engine,
    create_session_factory,
    dispose_engine,
    test_database_connection,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("API STARTING...")

    engine = create_engine()

    await test_database_connection(engine)

    create_session_factory(engine)

    logger.info("API STARTED SUCCESSFULLY")

    try:
        yield

    finally:

        logger.info("API SHUTTING DOWN...")

        await dispose_engine(engine)

        logger.info("API SHUTDOWN COMPLETE")


app = FastAPI(title="Police Fake News API", version="0.1.0", lifespan=lifespan)

setup_cors(app)
app.include_router(api_router)
register_exception_handlers(app)

print("🔥 CONNECTION MODULE IMPORTED")


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/")
async def root():
    return {"message": "API running"}


@app.get("/healthz")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        "src.api.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
