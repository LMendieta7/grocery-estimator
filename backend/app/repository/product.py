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
            .where(func.lower(ProductTable.name) == product_name.lower().strip())
        )

        row = self.db.execute(statement).first()
        
        return row
    
    def search_by_name(self, query: str):
        statement = (
            select(ProductTable, CategoryTable)
            .join(CategoryTable, ProductTable.category_id == CategoryTable.id)
            .where((ProductTable.name).ilike(f"%{query.strip()}%"))
            .order_by(ProductTable.name)
            .limit(50)
        )

        rows = self.db.execute(statement).all()

        return rows
    
    def create(self, product: ProductTable):
        self.db.add(product)
        self.db.flush()
        return product
    
    def delete(self, product):
        self.db.delete(product)
        self.db.flush()
        return product

    def get_product_by_id(self, product_id: int):
        statement = (
            select(ProductTable)
            .where(ProductTable.id == product_id)
        )
        return self.db.scalar(statement)

    def get_category_by_id(self, category_id: int):
        statement = (
            select(CategoryTable)
            .where(CategoryTable.id == category_id)
        )

        return self.db.scalar(statement)
    
