from pydantic import SecretStr, Field
from settings.base import AdvancedBaseSettings


class DatabaseSettings(AdvancedBaseSettings):
    host: str
    username: str
    password: SecretStr
    db_name: str = Field(..., env='db_name')
    port: int = Field(..., default='5432')

    class Config:
        env_prefix = 'DB_'

    @property
    def postgresql_url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"

def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings()
