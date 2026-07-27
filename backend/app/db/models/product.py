from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  String, Text, Numeric, DateTime, UniqueConstraint, ForeignKey

from decimal import Decimal

from backend.app.db.base import Base

class ProductTable(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(180), nullable=False, unique=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
    )

    estimated_price: Mapped[Decimal] = mapped_column(Numeric(10,2), default=Decimal("0.00"), nullable=False)
    image_url: Mapped[str | None] = mapped_column(Text, nullable=True)
