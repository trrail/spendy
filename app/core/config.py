from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    title: str = "Spendy"
    debug: bool = False

    # db_host: str
    # db_username: str
    # db_password: SecretStr
    # db_name: str
    # db_port: int = 5432

    class Config:
        allow_migrations = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

    # @property
    # def postgresql_url(self) -> str:
    #     return f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
