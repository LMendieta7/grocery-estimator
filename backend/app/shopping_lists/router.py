from fastapi import APIRouter, Depends, HTTPException

from backend.app.core.dependencies import get_shopping_list_service
from backend.app.shopping_lists.schemas import (
    GetAllListResponse,
    ShoppingListDetailResponse,
    ShoppingListItemCreateRequest,
)
from backend.app.shopping_lists.services import ShoppingListService


router = APIRouter()


@router.get("/shopping-lists", response_model=list[GetAllListResponse])
def get_all_shopping_lists(
    service: ShoppingListService = Depends(get_shopping_list_service),
):
    return service.get_all_lists()


@router.get(
    "/shopping-lists/{shopping_list_id}",
    response_model=ShoppingListDetailResponse,
)
def get_shopping_list_detail(
    shopping_list_id: int,
    service: ShoppingListService = Depends(get_shopping_list_service),
):
    list_detail = service.get_list_detail(shopping_list_id)
    if list_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Shopping list not found",
        )
    return list_detail


@router.post(
    "/shopping-lists/{shopping_list_id}/items",
    response_model=ShoppingListDetailResponse,
)
def add_shopping_list_item(
    request: ShoppingListItemCreateRequest,
    shopping_list_id: int,
    service: ShoppingListService = Depends(get_shopping_list_service),
):
    list_detail = service.add_item(shopping_list_id, request)
    if list_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Shopping list or product not found",
        )
    return list_detail


@router.delete(
    "/shopping-lists/{shopping_list_id}/items/{item_id}",
    response_model=ShoppingListDetailResponse,
)
def delete_shopping_list_item(
    shopping_list_id: int,
    item_id: int,
    service: ShoppingListService = Depends(get_shopping_list_service),
):
    list_detail = service.delete_item(shopping_list_id, item_id)
    if list_detail is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return list_detail
