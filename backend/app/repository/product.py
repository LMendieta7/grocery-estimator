from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.app.db.models.product import ProductTable
from backend.app.db.models.category import CategoryTable


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: int):
        # Fetch by primary key using the current database session.
        return self.db.get(ProductTable, product_id)

    def get_by_exact_name(self, product_name: str):
        statement = (
            select(ProductTable, CategoryTable)
            .join(CategoryTable, ProductTable.category_id == CategoryTable.id)
            .where(func.lower(ProductTable.name) == product_name.lower().strip())
        )

        return self.db.execute(statement).first()

    def search_by_name(self, query: str):
        statement = (
            select(ProductTable, CategoryTable)
            .join(CategoryTable, ProductTable.category_id == CategoryTable.id)
            .where(ProductTable.name.ilike(f"%{query.strip()}%"))
            .order_by(ProductTable.name)
            .limit(50)
        )

        return self.db.execute(statement).all()

    def create(self, product: ProductTable):
        self.db.add(product)
        self.db.flush()
        return product

    def delete(self, product: ProductTable):
        self.db.delete(product)
        self.db.flush()
        return product
    
    def update(self, product: ProductTable):
        self.db.flush()
        return product

    
