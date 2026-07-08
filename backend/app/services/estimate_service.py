from backend.app.models.grocery_item import GroceryItem
from backend.app.schemas.estimate import EstimateResponse, GroceryItemResponse


DEFAULT_ITEM_PRICE = 3.50

INVENTORY = [
    GroceryItem(name="milk", price=4.50),
    GroceryItem(name="bread", price=3.25),
    GroceryItem(name="eggs", price=5.00),
    GroceryItem(name="rice", price=6.50),
    GroceryItem(name="chicken", price=9.99),
    GroceryItem(name="apples", price=4.99),
    GroceryItem(name="bananas", price=2.25),
    GroceryItem(name="potatoes", price=4.75),
    GroceryItem(name="onions", price=3.50),
    GroceryItem(name="pasta", price=2.25),
]

INVENTORY_BY_NAME = {
    item.name.lower(): item
    for item in INVENTORY
}


def estimate_grocery_text(grocery_text: str) -> EstimateResponse:
    requested_names = [
        line.strip()
        for line in grocery_text.splitlines()
        if line.strip()
    ]

    response_items = []

    for name in requested_names:
        matched_item = INVENTORY_BY_NAME.get(name.lower())
        price = matched_item.price if matched_item else DEFAULT_ITEM_PRICE
        response_items.append(GroceryItemResponse(name=name, price=price))

    return EstimateResponse(
        items=response_items,
        item_count=len(response_items),
        estimated_total=round(sum(item.price for item in response_items), 2),
    )
