from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_env: str = Field(alias="APP_ENV", default="local")
    log_level: str = Field(alias="LOG_LEVEL", default="INFO")
    api_host: str = Field(alias="API_HOST", default="0.0.0.0")
    api_port: int = Field(alias="API_PORT", default=8000)


@lru_cache
def get_settings()->Settings:
    return Settings()
