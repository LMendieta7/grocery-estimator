from sqlalchemy import URL
from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseConfig:
    url: URL
    

database_config = DatabaseConfig(
   url= URL.create(
    "postgresql+psycopg",
    username="smart_grocery_user",
    password="smart_grocery_password",  # plain (unescaped) text
    host="localhost",
    database="smart_grocery",
    )
) 
