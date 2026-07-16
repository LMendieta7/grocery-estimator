from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.models.category import CategoryTable


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, category_id: int):
        statement = (
            select(CategoryTable)
            .where(CategoryTable.id == category_id)
        )

        return self.db.scalar(statement)
