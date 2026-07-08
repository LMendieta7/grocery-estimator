from typing import Protocol

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.db.models import GroceryInventoryRecord
from backend.app.models.grocery_item import GroceryItem


class GroceryRepository(Protocol):
    def find_by_name(self, *, store: str, name: str) -> GroceryItem | None:
        """Return an inventory item for a store, or None when unavailable."""


class InMemoryGroceryRepository:
    def __init__(self) -> None:
        inventory = [
            GroceryItem(name="Milk", unit="gallon", unit_price=4.29, store="Walmart"),
            GroceryItem(name="Eggs", unit="dozen", unit_price=3.99, store="Walmart"),
            GroceryItem(name="Bread (White)", unit="loaf", unit_price=2.49, store="Walmart"),
            GroceryItem(name="Chicken Breast", unit="lb", unit_price=4.49, store="Walmart"),
            GroceryItem(name="Bananas", unit="each", unit_price=0.69, store="Walmart"),
            GroceryItem(name="Rice", unit="bag", unit_price=5.49, store="Walmart"),
        ]

        self._items_by_store_and_name = {
            (item.store.lower(), item.name.lower()): item
            for item in inventory
        }
        self._items_by_store_and_name.update(
            {
                ("walmart", "bread"): inventory[2],
                ("walmart", "white bread"): inventory[2],
            }
        )

    def find_by_name(self, *, store: str, name: str) -> GroceryItem | None:
        return self._items_by_store_and_name.get((store.lower(), name.lower()))


class PostgresGroceryRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def find_by_name(self, *, store: str, name: str) -> GroceryItem | None:
        record = self._db.scalar(
            select(GroceryInventoryRecord).where(
                GroceryInventoryRecord.store == store,
                GroceryInventoryRecord.lookup_name == name.lower(),
            )
        )

        if record is None:
            return None

        return GroceryItem(
            name=record.name,
            unit=record.unit,
            unit_price=record.unit_price,
            store=record.store,
        )
