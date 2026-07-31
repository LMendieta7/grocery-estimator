from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.app.categories.models import CategoryTable
from backend.app.categories.schemas import GetAllCategoryResponse

class CategoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_categories(self):
        categories = self.db.scalars(
            select(CategoryTable).order_by(CategoryTable.id)
        ).all()

        return [GetAllCategoryResponse(
            id=category.id,
            name=category.name,
        )
            for category in categories
        ]


