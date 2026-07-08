from pydantic import BaseModel, Field


class GroceryEstimateRequest(BaseModel):
    store: str = Field(min_length=1, examples=["Walmart"])
    zip_code: str = Field(min_length=5, max_length=10, examples=["17601"])
    items_text: str = Field(
        min_length=1,
        examples=["2 gallons milk\n1 dozen eggs\n3 bananas"],
    )


class EstimatedItemResponse(BaseModel):
    name: str
    quantity: float
    unit: str
    unit_price: float | None
    total_price: float | None
    found: bool


class GroceryEstimateResponse(BaseModel):
    store: str
    zip_code: str
    estimated_total: float
    items_found: int
    items_not_found: int
    total_items: int
    items: list[EstimatedItemResponse]
