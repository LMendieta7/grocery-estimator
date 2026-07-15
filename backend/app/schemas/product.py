from pydantic import BaseModel, Field
from decimal import Decimal


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    estimated_price: Decimal
    image_url: str | None
    notes: str | None
