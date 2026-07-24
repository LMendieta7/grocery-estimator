from sqlalchemy import Boolean, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base


class ShoppingListItemTable(Base):
    __tablename__ = "shopping_list_items"

    __table_args__ = (
        UniqueConstraint(
            "shopping_list_id",
            "product_id",
            name="uq_shopping_list_product",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    shopping_list_id: Mapped[int] = mapped_column(
        ForeignKey("shopping_lists.id"),
        nullable=False,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    product_name_snapshot: Mapped[str] = mapped_column(Text, nullable=False)

    quantity: Mapped[int] = mapped_column(nullable=False, default=1)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Tracks whether this item has been checked off the list.
    is_checked: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
