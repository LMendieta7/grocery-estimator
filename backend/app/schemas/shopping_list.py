from pydantic import BaseModel
from sqlalchemy import DateTime
from datetime import datetime

class GetAllListResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
