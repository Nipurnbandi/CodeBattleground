from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    token_hours: int = 12
    judge0_url: str = "http://localhost:2358"
    callback_url: str = "http://host.docker.internal:8000"
    redis_url: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"


settings = Settings()