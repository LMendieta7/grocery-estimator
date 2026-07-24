from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.repository.shopping_list import ShoppingListRepository
from backend.app.repository.shopping_list_item import ShoppingListItemRepository
from backend.app.services.shopping_list import ShoppingListService
from backend.app.db.session import get_db
from backend.app.schemas.shopping_list import GetAllListResponse, ShoppingListDetailResponse


router = APIRouter()


@router.get("/shopping-lists", response_model=list[GetAllListResponse])
def get_all_shopping_lists(
    db: Session = Depends(get_db),
):
    # Repository and service will go here.
    list_repository = ShoppingListRepository(db)
    list_item_repository = ShoppingListItemRepository(db)
    list_service = ShoppingListService(db, list_repository, list_item_repository)

    shopping_lists = list_service.get_all_lists()
    return shopping_lists

@router.get("/shopping-lists/{shopping_list_id}", response_model=ShoppingListDetailResponse)
def get_shopping_list_detail(
    shopping_list_id: int,
    db: Session = Depends(get_db),
):
    
    list_repository = ShoppingListRepository(db)
    list_item_repository = ShoppingListItemRepository(db)
    list_service = ShoppingListService(db, list_repository, list_item_repository)

    list_detail = list_service.get_list_detail(shopping_list_id)

    if list_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Shopping list not found",
        )

    return list_detail


    