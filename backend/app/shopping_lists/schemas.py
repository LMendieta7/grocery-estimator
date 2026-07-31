from datetime import datetime
from decimal import Decimal
from enum import StrEnum

from pydantic import BaseModel, Field


class ItemUnit(StrEnum):
    EACH = "each"
    PACK = "pack"
    POUND = "lb"
    OUNCE = "oz"
    KILOGRAM = "kg"
    GRAM = "g"
    LITER = "L"
    MILLILITER = "mL"
    GALLON = "gallon"
    DOZEN = "dozen"


class ShoppingListItemCreateRequest(BaseModel):
    product_id: int
    quantity: Decimal = Field(default=Decimal("1.00"), gt=0)
    unit: ItemUnit = ItemUnit.EACH
    image_url: str | None = None
    notes: str | None = None


class ShoppingListItemResponse(BaseModel):
    id: int
    shopping_list_id: int
    product_id: int
    product_name: str
    category_id: int
    category: str
    quantity: Decimal
    unit: ItemUnit
    estimated_price: Decimal | None
    image_url: str | None
    notes: str | None
    is_checked: bool


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
    estimated_total: Decimal | None


class ShoppingListItemUpdateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    category_id: int | None = Field(default=None, ge=1)
    quantity: Decimal | None = Field(default=None, gt=0)
    unit: ItemUnit | None = None
    estimated_price: Decimal | None = Field(default=None, ge=0)
    image_url: str | None = None
    notes: str | None = None
    is_checked: bool | None = None

class ShoppingListItemMutationResponse(BaseModel):
    message: str
    list_id: int
    list_item_id: int
    item_name: str
