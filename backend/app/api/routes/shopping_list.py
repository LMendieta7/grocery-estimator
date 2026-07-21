from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.repository.shopping_list import ShoppingListRepository
from backend.app.services.shopping_list import ShoppingListService
from backend.app.db.session import get_db
from backend.app.schemas.shopping_list import GetAllListResponse

router = APIRouter()


@router.get("/shopping-lists", response_model=list[GetAllListResponse])
def get_all_shopping_lists(
    db: Session = Depends(get_db),
):
    # Repository and service will go here.
    repository = ShoppingListRepository(db)
    service = ShoppingListService(db, repository)

    shopping_lists = service.get_all_lists()
    return shopping_lists