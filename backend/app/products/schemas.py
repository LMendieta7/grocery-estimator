from decimal import Decimal

from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    estimated_price: Decimal
    image_url: str | None


class ProductMutationResponse(BaseModel):
    message: str
    product_id: int
    product_name: str


class ProductCreateRequest(BaseModel):
    name: str = Field(min_length=1)
    category_id: int
    estimated_price: Decimal | None = None
    image_url: str | None = None


class ProductUpdateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    category_id: int | None = None
    estimated_price: Decimal | None = None
    image_url: str | None = None
