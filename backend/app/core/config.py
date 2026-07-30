from dataclasses import dataclass

from sqlalchemy import URL


@dataclass(frozen=True)
class DatabaseConfig:
    url: URL


database_config = DatabaseConfig(
    url=URL.create(
        "postgresql+psycopg",
        username="smart_grocery_user",
        password="smart_grocery_password",
        host="localhost",
        database="smart_grocery",
    )
)
