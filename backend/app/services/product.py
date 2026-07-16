from decimal import Decimal

from backend.app.schemas.product import ProductResponse
from backend.app.db.models.product import ProductTable


class ProductService:
    def __init__(self, product_repository, db):
        self.product_repository = product_repository
        self.db = db

    def get_product_by_exact_name(self, product_name: str):
        row = self.product_repository.get_by_exact_name(product_name)

        if row is None:
            return None
        
        product, category = row
    
        return ProductResponse(
            id=product.id,
            name=product.name,
            category=category.name,
            estimated_price=product.estimated_price,
            image_url=product.image_url,
            notes=product.notes,
        )
    
    def search_products_by_name(self, query: str):
        rows = self.product_repository.search_by_name(query)

        return [ProductResponse(
            id=product.id,
            name=product.name,
            category=category.name,
            estimated_price=product.estimated_price,
            image_url=product.image_url,
            notes=product.notes,
        )
        for product, category in rows
        ]
    
    def create_product(self, request):
        category = self.product_repository.get_category_by_id(request.category_id)

        if category is None:
            return None

        product = ProductTable(
            name=request.name,
            category_id=category.id,
            estimated_price=request.estimated_price or Decimal("0.00"),
            image_url=request.image_url,
            notes=request.notes
        )

        product = self.product_repository.create(product)

        self.db.commit()

        return ProductResponse(
            id=product.id,
            name=product.name,
            category=category.name,
            estimated_price=product.estimated_price,
            image_url=product.image_url,
            notes=product.notes,
        )

    def delete_product(self, product_id):
        product = self.product_repository.get_product_by_id(product_id)

        if product is None:
            return None
       
        self.product_repository.delete(product)

        self.db.commit()
        return product
