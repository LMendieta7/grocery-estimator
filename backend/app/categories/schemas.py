from pydantic import BaseModel, Field

class GetAllCategoryResponse(BaseModel):
    id: int
    name: str
    