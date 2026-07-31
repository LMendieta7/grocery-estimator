from fastapi import APIRouter, Depends, HTTPException
from backend.app.core.dependencies import get_categories_service
from backend.app.categories.schemas import GetAllCategoryResponse
from backend.app.categories.services import CategoryService

router = APIRouter()

@router.get("/categories", response_model=list[GetAllCategoryResponse])
def get_all_shopping_lists(
    service: CategoryService = Depends(get_categories_service),
):
    return service.get_all_categories()
