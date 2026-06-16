import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# =========================================================
# LOGGING
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# =========================================================
# LOAD ENV
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[3]

dotenv_path = BASE_DIR / ".env"

logger.info(f"BASE_DIR: {BASE_DIR}")
logger.info(f".env exists: {dotenv_path.exists()}")

load_dotenv(dotenv_path)

# =========================================================
# DATABASE URL
# =========================================================

DATABASE_URL = os.getenv("DATABASE_URL")

logger.info(f"DATABASE_URL ORIGINAL: {DATABASE_URL}")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL NOT DEFINED")

# =========================================================
# CONVERT TO ASYNC SQLALCHEMY URL
# =========================================================

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+asyncpg://",
        1
    )

elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+asyncpg://",
        1
    )

logger.info(f"DATABASE_URL FINAL: {DATABASE_URL}")

# =========================================================
# SQLALCHEMY ENGINE
# =========================================================

_engine: AsyncEngine | None = None

_session_factory: async_sessionmaker[AsyncSession] | None = None


def create_engine() -> AsyncEngine:
    """
    Create singleton async engine.
    """

    global _engine

    if _engine is None:
        logger.info("CREATING SQLALCHEMY ENGINE...")

        _engine = create_async_engine(
            DATABASE_URL,
            echo=True,
            pool_pre_ping=True,

            # IMPORTANT FOR RENDER POSTGRES
            connect_args={
                "ssl": "require"
            }
        )

        logger.info("ENGINE CREATED SUCCESSFULLY")

    return _engine


def create_session_factory(
        engine: AsyncEngine
) -> async_sessionmaker[AsyncSession]:
    """
    Create singleton session factory.
    """

    global _session_factory

    if _session_factory is None:
        logger.info("CREATING SESSION FACTORY...")

        _session_factory = async_sessionmaker(
            bind=engine,
            expire_on_commit=False,
        )

        logger.info("SESSION FACTORY CREATED")

    return _session_factory


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    if _session_factory is None:
        raise RuntimeError(
            "Session factory not initialized"
        )

    return _session_factory


async def dispose_engine(
        engine: AsyncEngine
) -> None:
    logger.info("DISPOSING ENGINE...")

    await engine.dispose()

    logger.info("ENGINE DISPOSED")


# =========================================================
# TEST DATABASE CONNECTION
# =========================================================

async def test_database_connection(
        engine: AsyncEngine
) -> None:
    logger.info("TESTING DATABASE CONNECTION...")

    try:

        async with engine.begin() as conn:

            logger.info("CONNECTED TO DATABASE")

            result = await conn.execute(
                text("SELECT 1")
            )

            logger.info(
                f"TEST QUERY RESULT: {result.scalar()}"
            )

            logger.info(
                "DATABASE CONNECTION SUCCESS"
            )

    except Exception as e:

        logger.exception(
            "DATABASE CONNECTION FAILED"
        )

        raise e


# =========================================================
# FASTAPI DEPENDENCY
# =========================================================

async def get_session():
    session_factory = get_session_factory()

    async with session_factory() as session:

        logger.info("OPENING DATABASE SESSION")

        try:
            yield session

        finally:
            logger.info("CLOSING DATABASE SESSION")


# =========================================================
# REDIS
# =========================================================

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

REDIS_URL = (
    f"redis://"
    f"{f':{REDIS_PASSWORD}@' if REDIS_PASSWORD else ''}"
    f"{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
)

logger.info(f"REDIS_URL: {REDIS_URL}")

# =========================================================
# RABBITMQ
# =========================================================

RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/")

RABBITMQ_URL = (
    f"amqp://"
    f"{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@"
    f"{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
    f"{RABBITMQ_VHOST}"
)

logger.info(f"RABBITMQ_URL: {RABBITMQ_URL}")

# =========================================================
# JWT
# =========================================================

JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "your_secret_jwt_key_here"
)

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256"
)

JWT_EXPIRATION_MINUTES = int(
    os.getenv("JWT_EXPIRATION_MINUTES", 60)
)

# =========================================================
# APP CONFIG
# =========================================================

APP_ENV = os.getenv("APP_ENV", "development")

APP_DEBUG = (
        os.getenv("APP_DEBUG", "True").lower()
        in ["true", "1"]
)

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")

APP_PORT = int(
    os.getenv("APP_PORT", 8000)
)

logger.info(f"APP_ENV: {APP_ENV}")
logger.info(f"APP_DEBUG: {APP_DEBUG}")

# =========================================================
# SCRAPING / WORKERS
# =========================================================

SCRAPING_TIMEOUT = int(
    os.getenv("SCRAPING_TIMEOUT", 30)
)

MAX_WORKERS = int(
    os.getenv("MAX_WORKERS", 5)
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "DEBUG"
)

logger.info("DATABASE MODULE LOADED")
