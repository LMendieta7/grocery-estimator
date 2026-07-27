from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from backend.app.repository.shopping_list_item import ShoppingListItemRepository
from backend.app.repository.shopping_list import ShoppingListRepository
from backend.app.repository.product import ProductRepository
from backend.app.services.shopping_list import ShoppingListService
from backend.app.db.session import get_db
from backend.app.schemas.shopping_list_item import ShoppingListItemCreateRequest
from backend.app.schemas.shopping_list import ShoppingListDetailResponse
router = APIRouter()


@router.post("/shopping-lists/{shopping_list_id}/items", response_model=ShoppingListDetailResponse)
def add_shopping_list_item(
    request: ShoppingListItemCreateRequest,
    shopping_list_id: int,
    db: Session = Depends(get_db),
):
    # Repository and service will go here.

    shopping_list_item_repository = ShoppingListItemRepository(db)
    shopping_list_repository = ShoppingListRepository(db)
    product_repository = ProductRepository(db)

    list_service = ShoppingListService(
        db,
        shopping_list_repository,
        shopping_list_item_repository,
        product_repository,
    )

    list_detail = list_service.add_item(shopping_list_id, request)
    
    if list_detail is None:
        raise HTTPException(status_code=404, detail="Shopping list or product not found")

    return list_detail

@router.delete("/shopping-lists/{shopping_list_id}/items/{item_id}", response_model=ShoppingListDetailResponse)
def delete_list_item(
    shopping_list_id:int,
    item_id:int,
    db: Session= Depends(get_db)
):
    shopping_list_repository = ShoppingListRepository(db)
    shopping_list_item_repository = ShoppingListItemRepository(db)
    product_repository = ProductRepository(db)

    list_service = ShoppingListService(
        db,
        shopping_list_repository,
        shopping_list_item_repository,
        product_repository,
    )
    list_detail = list_service.delete_item(shopping_list_id, item_id)

    if list_detail is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return list_detail
