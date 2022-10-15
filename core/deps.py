# DEPENDENCIAS
from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        # Usa, aguarda e devolve a sessao para uso
        yield session
    finally:
        # fecha sessao apos o uso
        await session.close()