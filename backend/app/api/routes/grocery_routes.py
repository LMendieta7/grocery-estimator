from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.db.session import get_db_session
from backend.app.repositories.grocery_repository import (
    GroceryRepository,
    InMemoryGroceryRepository,
    PostgresGroceryRepository,
)
from backend.app.schemas.grocery_schema import (
    GroceryEstimateRequest,
    GroceryEstimateResponse,
)
from backend.app.services.grocery_estimate_service import GroceryEstimateService

router = APIRouter()


def get_grocery_repository(
    db: Session = Depends(get_db_session),
) -> GroceryRepository:
    if settings.repository_backend == "postgres":
        return PostgresGroceryRepository(db)

    return InMemoryGroceryRepository()


def get_grocery_estimate_service(
    repository: GroceryRepository = Depends(get_grocery_repository),
) -> GroceryEstimateService:
    return GroceryEstimateService(repository)


@router.post("/estimate", response_model=GroceryEstimateResponse)
def estimate_grocery_list(
    request: GroceryEstimateRequest,
    service: GroceryEstimateService = Depends(get_grocery_estimate_service),
) -> GroceryEstimateResponse:
    return service.estimate(
        store=request.store,
        zip_code=request.zip_code,
        items_text=request.items_text,
    )
