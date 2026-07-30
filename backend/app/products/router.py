from fastapi import APIRouter, Depends, HTTPException, Query

from backend.app.core.dependencies import get_product_service
from backend.app.products.schemas import (
    ProductCreateRequest,
    ProductMutationResponse,
    ProductResponse,
    ProductUpdateRequest,
)
from backend.app.products.services import ProductService


router = APIRouter()


@router.get("/products/by-name", response_model=ProductResponse)
def get_product_by_exact_name(
    name: str = Query(min_length=1),
    service: ProductService = Depends(get_product_service),
):
    product = service.get_product_by_exact_name(name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/products/search", response_model=list[ProductResponse])
def search_products(
    q: str = Query(min_length=1),
    service: ProductService = Depends(get_product_service),
):
    return service.search_products_by_name(q)


@router.post("/products/", response_model=ProductResponse)
def create_product(
    request: ProductCreateRequest,
    service: ProductService = Depends(get_product_service),
):
    product = service.create_product(request)
    if product is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return product


@router.delete("/products/{product_id}", response_model=ProductMutationResponse)
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service),
):
    product = service.delete_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "message": "Product deleted",
        "product_id": product.id,
        "product_name": product.name,
    }


@router.patch(
    "/products/{product_id}",
    response_model=ProductMutationResponse,
)
def update_product(
    product_id: int,
    request: ProductUpdateRequest,
    service: ProductService = Depends(get_product_service),
):
    product = service.update_product(product_id, request)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product or category not found",
        )

    return {
        "message": "Product updated",
        "product_id": product.id,
        "product_name": product.name,
    }
