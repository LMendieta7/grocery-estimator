from sqlalchemy import select, func
from backend.app.db.models.product import ProductTable
from backend.app.db.models.category import CategoryTable



class ProductRepository:
    def __init__(self, db):
        self.db = db

    def get_by_exact_name(self, product_name: str):
        statement = (
            select(ProductTable, CategoryTable)
            .join(CategoryTable, ProductTable.category_id == CategoryTable.id)
            .where(func.lower(ProductTable.name) == product_name.lower())
        )

        row = self.db.execute(statement).first()
        
        return row


        

        
