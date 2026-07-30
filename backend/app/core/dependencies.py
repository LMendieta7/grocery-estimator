from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.core.database import SessionLocal
from backend.app.products.services import ProductService
from backend.app.shopping_lists.services import ShoppingListService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_product_service(
    db: Session = Depends(get_db),
) -> ProductService:
    return ProductService(db)


def get_shopping_list_service(
    db: Session = Depends(get_db),
) -> ShoppingListService:
    return ShoppingListService(db)
