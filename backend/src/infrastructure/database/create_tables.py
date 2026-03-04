import asyncio
from src.infrastructure.database.base import Base
from src.infrastructure.database.connection import create_engine
import sys
from pathlib import Path

# Adiciona a raiz do projeto ao path
sys.path.append(str(Path(__file__).resolve().parents[2]))

async def create_tables():
    # Cria o AsyncEngine
    engine = create_engine()

    # Abre uma conexão de contexto com begin(), para poder rodar comandos de DDL
    async with engine.begin() as conn:
        # Apaga todas as tabelas existentes
        await conn.run_sync(Base.metadata.drop_all)
        # Cria todas as tabelas definidas no Base
        await conn.run_sync(Base.metadata.create_all)

    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    asyncio.run(create_tables())

