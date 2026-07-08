from pydantic import BaseModel, Field


class EstimateRequest(BaseModel):
    grocery_text: str = Field(
        min_length=1,
        examples=["milk\nbread\neggs"],
    )

class GroceryItemResponse(BaseModel):
    name: str
    price: float

class EstimateResponse(BaseModel):
    items: list[GroceryItemResponse]
    item_count: int
    estimated_total: float
