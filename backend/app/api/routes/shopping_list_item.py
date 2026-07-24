from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from backend.app.repository.shopping_list_item import ShoppingListItemRepository
from backend.app.repository.shopping_list import ShoppingListRepository
from backend.app.repository.product import ProductRepository
from backend.app.services.shopping_list_item import ShoppingListItemService
from backend.app.db.session import get_db
from backend.app.schemas.shopping_list_item import ShoppingListItemResponse, ShoppingListItemCreateRequest

router = APIRouter()


@router.post("/shopping-lists/{shopping_list_id}/items", response_model=ShoppingListItemResponse)
def add_shopping_list_item(
    request: ShoppingListItemCreateRequest,
    shopping_list_id: int,
    db: Session = Depends(get_db),
):
    # Repository and service will go here.
    shopping_list_item_repository = ShoppingListItemRepository(db)
    shopping_list_repository = ShoppingListRepository(db)
    product_repository = ProductRepository(db)

    service = ShoppingListItemService(
        db,
        shopping_list_repository,
        shopping_list_item_repository,
        product_repository,
    )

    item = service.add_item(shopping_list_id, request)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Shopping list or product not found")
    return item