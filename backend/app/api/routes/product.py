from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.schemas.product import ProductResponse, ProductCreateRequest, DeleteProductResponse

from backend.app.services.product import ProductService
from backend.app.repository.product import ProductRepository

router = APIRouter()


@router.get("/products/by-name", response_model=ProductResponse)
def get_product_by_exact_name(
    name: str = Query(min_length=1),
    db: Session = Depends(get_db),
):
    repository = ProductRepository(db)
    service = ProductService(repository, db)
    
    product = service.get_product_by_exact_name(name)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

@router.get("/products/search", response_model=list[ProductResponse])
def search_products(
    q: str = Query(min_length=1),
    db: Session = Depends(get_db),
):
    repository = ProductRepository(db)
    service = ProductService(repository, db)
    
    return service.search_products_by_name(q)


@router.post("/products/", response_model=ProductResponse)
def create_products(
    request: ProductCreateRequest,
    db: Session = Depends(get_db),
):
    repository = ProductRepository(db)
    service = ProductService(repository, db)
    product = service.create_product(request)

    if product is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return product

@router.delete("/products/{product_id}", response_model=DeleteProductResponse)
def delete_products(
    product_id: int,
    db: Session = Depends(get_db),
):
    repository = ProductRepository(db)
    service = ProductService(repository, db)
    product = service.delete_product(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    
    return {
        "message": "Product deleted", 
        "product_id": product.id,
        "product_name": product.name,
    }
