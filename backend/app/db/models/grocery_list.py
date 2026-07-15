from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import  Text, DateTime
from datetime import datetime, timezone

from backend.app.db.base import Base

class GroceryListTable(Base):
    __tablename__ = "grocery_lists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Tracks when the grocery list was created.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
