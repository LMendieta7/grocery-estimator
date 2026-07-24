from pydantic import BaseModel, Field
from decimal import Decimal

class ShoppingListItemCreateRequest(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1)
    notes: str | None = None


class ShoppingListItemResponse(BaseModel):
    id: int
    shopping_list_id: int
    product_id: int
    product_name_snapshot: str
    category: str
    quantity: int
    estimated_price: Decimal
    notes: str | None
    is_checked: bool