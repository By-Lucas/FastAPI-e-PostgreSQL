# CONFIGURACOES
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'

    # Fazer execução assincrona no banco de dados
    DB_URL: str = "postgresql+asyncpg://postgres:123@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        """ Para manter, EX: se for maiusculo fica tudo maiusculo ou se minusculo fica tudo minusculo"""
        case_sensitive = True

settings = Settings()