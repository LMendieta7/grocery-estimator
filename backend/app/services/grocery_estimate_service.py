from dataclasses import replace

from backend.app.models.grocery_item import EstimatedItem
from backend.app.repositories.grocery_repository import GroceryRepository
from backend.app.schemas.grocery_schema import (
    EstimatedItemResponse,
    GroceryEstimateResponse,
)


KNOWN_UNITS = {
    "bag",
    "bags",
    "bottle",
    "bottles",
    "dozen",
    "each",
    "gallon",
    "gallons",
    "lb",
    "lbs",
    "loaf",
    "loaves",
    "pack",
    "packs",
}

UNIT_NORMALIZATION = {
    "gallons": "gallon",
    "lbs": "lb",
    "loaves": "loaf",
    "bags": "bag",
    "bottles": "bottle",
    "packs": "pack",
}


class GroceryEstimateService:
    def __init__(self, repository: GroceryRepository) -> None:
        self._repository = repository

    def estimate(
        self,
        *,
        store: str,
        zip_code: str,
        items_text: str,
    ) -> GroceryEstimateResponse:
        estimated_items = [
            self._estimate_line(store=store, line=line)
            for line in self._non_empty_lines(items_text)
        ]

        estimated_total = sum(item.total_price or 0 for item in estimated_items)
        items_found = sum(1 for item in estimated_items if item.found)

        return GroceryEstimateResponse(
            store=store,
            zip_code=zip_code,
            estimated_total=round(estimated_total, 2),
            items_found=items_found,
            items_not_found=len(estimated_items) - items_found,
            total_items=len(estimated_items),
            items=[self._to_response_item(item) for item in estimated_items],
        )

    def _estimate_line(self, *, store: str, line: str) -> EstimatedItem:
        quantity, unit, item_name = self._parse_line(line)
        inventory_item = self._repository.find_by_name(store=store, name=item_name)

        if inventory_item is None:
            return EstimatedItem(
                name=item_name.title(),
                quantity=quantity,
                unit=unit,
                unit_price=None,
                total_price=None,
                found=False,
            )

        unit_price = inventory_item.unit_price
        resolved = EstimatedItem(
            name=inventory_item.name,
            quantity=quantity,
            unit=unit if unit != "each" else inventory_item.unit,
            unit_price=unit_price,
            total_price=round(quantity * unit_price, 2),
            found=True,
        )

        if resolved.unit != inventory_item.unit:
            return replace(resolved, unit=unit)

        return resolved

    def _parse_line(self, line: str) -> tuple[float, str, str]:
        parts = line.strip().split()

        if not parts:
            return 1, "each", ""

        quantity = self._parse_quantity(parts[0])
        start_index = 1 if quantity is not None else 0
        quantity = quantity or 1

        unit = "each"
        if len(parts) > start_index and parts[start_index].lower() in KNOWN_UNITS:
            unit = self._normalize_unit(parts[start_index])
            start_index += 1

        item_name = " ".join(parts[start_index:]).strip()
        return quantity, unit, item_name

    def _parse_quantity(self, value: str) -> float | None:
        try:
            return float(value)
        except ValueError:
            return None

    def _normalize_unit(self, unit: str) -> str:
        return UNIT_NORMALIZATION.get(unit.lower(), unit.lower())

    def _non_empty_lines(self, items_text: str) -> list[str]:
        return [line.strip() for line in items_text.splitlines() if line.strip()]

    def _to_response_item(self, item: EstimatedItem) -> EstimatedItemResponse:
        return EstimatedItemResponse(
            name=item.name,
            quantity=item.quantity,
            unit=item.unit,
            unit_price=item.unit_price,
            total_price=item.total_price,
            found=item.found,
        )
