from decimal import Decimal

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.app.categories.models import CategoryTable
from backend.app.products.models import ProductTable
from backend.app.products.schemas import ProductResponse


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_exact_name(self, product_name: str):
        statement = (
            select(ProductTable, CategoryTable)
            .join(CategoryTable, ProductTable.category_id == CategoryTable.id)
            .where(
                func.lower(ProductTable.name)
                == product_name.lower().strip()
            )
        )
        row = self.db.execute(statement).first()
        if row is None:
            return None

        product, category = row
        return self._to_response(product, category)

    def search_products_by_name(self, query: str):
        statement = (
            select(ProductTable, CategoryTable)
            .join(CategoryTable, ProductTable.category_id == CategoryTable.id)
            .where(ProductTable.name.ilike(f"%{query.strip()}%"))
            .order_by(ProductTable.name)
            .limit(50)
        )
        rows = self.db.execute(statement).all()
        return [
            self._to_response(product, category)
            for product, category in rows
        ]

    def create_product(self, request):
        category = self.db.get(CategoryTable, request.category_id)
        if category is None:
            return None

        product = ProductTable(
            name=request.name,
            category_id=category.id,
            estimated_price=request.estimated_price or Decimal("0.00"),
            image_url=request.image_url,
        )
        self.db.add(product)
        self.db.flush()
        self.db.commit()

        return self._to_response(product, category)

    def delete_product(self, product_id):
        product = self.db.get(ProductTable, product_id)
        if product is None:
            return None

        self.db.delete(product)
        self.db.commit()
        return product

    def update_product(self, product_id, request):
        product = self.db.get(ProductTable, product_id)
        if product is None:
            return None

        update_data = request.model_dump(exclude_unset=True)
        if "category_id" in update_data:
            category = self.db.get(CategoryTable, update_data["category_id"])
            if category is None:
                return None

        for field, value in update_data.items():
            setattr(product, field, value)

        self.db.commit()
        self.db.refresh(product)
        return product

    @staticmethod
    def _to_response(product, category):
        return ProductResponse(
            id=product.id,
            name=product.name,
            category=category.name,
            estimated_price=product.estimated_price,
            image_url=product.image_url,
        )
