from fastapi import HTTPException

from backend.app.schemas.product import ProductResponse



class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_product_by_exact_name(self, product_name: str):
        row = self.product_repository.get_by_exact_name(product_name)

        if row is None:
            raise HTTPException(status_code=404, detail="Product not found")

        product, category = row
    
        return ProductResponse(
            id=product.id,
            name=product.name,
            category=category.name,
            estimated_price=product.estimated_price,
            image_url=product.image_url,
            notes=product.notes,
        )
    
