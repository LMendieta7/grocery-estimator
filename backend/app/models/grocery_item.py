from dataclasses import dataclass


@dataclass(frozen=True)
class GroceryItem:
    name: str
    unit: str
    unit_price: float
    store: str


@dataclass(frozen=True)
class EstimatedItem:
    name: str
    quantity: float
    unit: str
    unit_price: float | None
    total_price: float | None
    found: bool
