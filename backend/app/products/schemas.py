from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str


class ProductMutationResponse(BaseModel):
    message: str
    product_id: int
    product_name: str


class ProductCreateRequest(BaseModel):
    name: str = Field(min_length=1)
    category_id: int


class ProductUpdateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    category_id: int | None = None
