from pydantic import BaseModel, Field
from decimal import Decimal


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    estimated_price: Decimal
    image_url: str | None
    notes: str | None

class DeleteProductResponse(BaseModel):
    message: str
    product_id: int
    product_name: str

class ProductCreateRequest(BaseModel):
    name: str = Field(min_length=1)
    category_id: int
    estimated_price: Decimal | None = None
    image_url: str | None = None
    notes: str | None = None
