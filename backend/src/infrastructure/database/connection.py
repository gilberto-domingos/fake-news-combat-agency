# src/infrastructure/database/connection.py
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[3]  # Adjust to your structure level
load_dotenv(BASE_DIR / ".env")

# ==========================================
# DATABASE (PostgreSQL Async)
# ==========================================
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker

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


# FastAPI Dependency
async def get_session() -> AsyncSession:
    async with get_session_factory()() as session:
        yield session

# ==========================================
# REDIS (Cache / Queue)
# ==========================================
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

REDIS_URL = f"redis://{f':{REDIS_PASSWORD}@' if REDIS_PASSWORD else ''}{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# ==========================================
# RABBITMQ (Broker)
# ==========================================
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/")

RABBITMQ_URL = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}"

# ==========================================
# JWT / Authentication
# ==========================================
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_jwt_key_here")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES", 60))

# ==========================================
# App / FastAPI Config
# ==========================================
APP_ENV = os.getenv("APP_ENV", "development")
APP_DEBUG = os.getenv("APP_DEBUG", "True").lower() in ["true", "1"]
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", 8000))

# ==========================================
# Scraping / Workers / Logging
# ==========================================
SCRAPING_TIMEOUT = int(os.getenv("SCRAPING_TIMEOUT", 30))
MAX_WORKERS = int(os.getenv("MAX_WORKERS", 5))
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")