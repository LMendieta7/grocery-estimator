from sqlalchemy import Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.session import Base


class GroceryInventoryRecord(Base):
    __tablename__ = "grocery_inventory"
    __table_args__ = (
        UniqueConstraint("store", "lookup_name", name="uq_grocery_inventory_store_lookup"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    lookup_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    unit: Mapped[str] = mapped_column(String(40), nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    store: Mapped[str] = mapped_column(String(80), nullable=False, index=True)
