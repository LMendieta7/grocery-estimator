from pydantic import BaseModel
from datetime import datetime
from backend.app.schemas.shopping_list_item import ShoppingListItemResponse
from decimal import Decimal

class GetAllListResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

class ShoppingListDetailResponse(BaseModel):
    id: int
    name: str
    items: list[ShoppingListItemResponse]
    checked_count: int
    total_count: int
    estimated_total: Decimal
