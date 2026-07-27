from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.models.shopping_list_item import ShoppingListItemTable
from backend.app.db.models.category import CategoryTable
from backend.app.db.models.product import ProductTable

class ShoppingListItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, item_id: int):
        return self.db.get(ShoppingListItemTable, item_id)

    def get_by_list_id(self, shopping_list_id: int):
        statement = (
            select(ShoppingListItemTable)
            .where(
                ShoppingListItemTable.shopping_list_id
                == shopping_list_id
            )
            .order_by(ShoppingListItemTable.id)
        )

        return self.db.scalars(statement).all()
    
    def get_items_with_product_details(self, shopping_list_id):
        statement= (
            select(ShoppingListItemTable, ProductTable, CategoryTable)
            .join(
                ProductTable,
                ShoppingListItemTable.product_id == ProductTable.id,
                
            )
            .join(CategoryTable,
                  ProductTable.category_id == CategoryTable.id
                  )
            .where(ShoppingListItemTable.shopping_list_id == shopping_list_id)
            .order_by(ShoppingListItemTable.id)
        )
        return self.db.execute(statement).all()

    def create(self, item: ShoppingListItemTable):
        self.db.add(item)
        self.db.flush()
        return item

    def delete(self, item: ShoppingListItemTable):
        self.db.delete(item)
        self.db.flush()
        