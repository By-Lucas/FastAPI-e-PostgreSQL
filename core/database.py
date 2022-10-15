# BANCO DE DADOS
from re import S
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings

# Criação das tabelas
engine: AsyncEngine = create_async_engine(settings.DB_URL)


# Sera usado para abrir e fechar conexão com banco de dados
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

