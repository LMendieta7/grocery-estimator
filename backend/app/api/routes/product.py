from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.schemas.product import ProductResponse

from backend.app.services.product import ProductService
from backend.app.repository.product import ProductRepository

router = APIRouter()


@router.get("/product/", response_model=ProductResponse)
def get_product_by_exact_name(
    q: str,
    db: Session = Depends(get_db),
):
    repository = ProductRepository(db)
    service = ProductService(repository)
    
    return service.get_product_by_exact_name(q)


# @router.post("/products/bulk/prices", response_model=list[ProductPriceResponse])
# def get_product_prices_by_store(
#     request: ProductSearchRequest,
#     db: Session = Depends(get_db),
# ):
#     repository = ProductRepository(db)
#     service = ProductService(repository)
#     return service.get_prices_by_product_name(request.product, request.store)
