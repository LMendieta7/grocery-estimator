from fastapi import APIRouter

from backend.app.schemas.estimate import EstimateRequest, EstimateResponse
from backend.app.services.estimate_service import estimate_grocery_text

router = APIRouter()


@router.post("/estimate", response_model=EstimateResponse)
def estimate_grocery_list(request: EstimateRequest):
    return estimate_grocery_text(request.grocery_text)
