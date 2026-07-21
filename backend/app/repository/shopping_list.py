from sqlalchemy.orm import Session
from sqlalchemy import select

from backend.app.db.models.shopping_list import ShoppingListTable

class ShoppingListRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, list_id: int):
        # Fetch by primary key using the current database session.
        return self.db.get(ShoppingListTable, list_id)
    
    def get_all_lists(self):
        return self.db.scalars(
            select(ShoppingListTable).order_by(ShoppingListTable.id)
        ).all()