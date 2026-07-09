
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.core.database_config import database_config
#example
# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")
DATABASE_URL = database_config.url

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

