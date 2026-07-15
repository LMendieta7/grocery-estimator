from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base


class GroceryListItemTable(Base):
    __tablename__ = "grocery_list_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    grocery_list_id: Mapped[int] = mapped_column(
        ForeignKey("grocery_lists.id"),
        nullable=False,
    )

    product_id: Mapped[int | None] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )
    
    product_name_snapshot: Mapped[str] = mapped_column(Text, nullable=False)

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        default=1,
    )

    estimated_unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        default=0.0
    )

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Tracks whether this item has been checked off the list.
    is_checked: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
