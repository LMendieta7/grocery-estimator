from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  String

from backend.app.db.base import Base

class CategoryTable(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)