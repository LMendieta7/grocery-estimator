from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Grocery Estimator API"
    database_url: str = (
        "postgresql+psycopg://grocery_user:grocery_password@localhost:5432/grocery_app"
    )
    repository_backend: str = "memory"
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    model_config = SettingsConfigDict(env_prefix="GROCERY_")


settings = Settings()
