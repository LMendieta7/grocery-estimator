from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.models.category import CategoryTable


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, category_id: int):
        # Fetch by primary key using the current database session.
        return self.db.get(CategoryTable, category_id)
