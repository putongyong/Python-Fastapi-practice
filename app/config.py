from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: PostgresDsn
    db_test_url: PostgresDsn

    pythonpath: str

    postgres_db:str
    postgres_user:str
    postgres_password:str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings

if __name__ == "__main__":
    settings = get_settings()
