from pydantic_settings import (SettingsConfigDict, BaseSettings)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    DATABASE_URL: str
