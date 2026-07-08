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
    response_items = []

    for line in grocery_text.splitlines():
        line = line.strip()
        if not line:
            continue

        parts = line.split(maxsplit=1)
        if parts[0].isdigit() and len(parts) >=2:
            quantity = int(parts[0])
            name = parts[1]
        else:
            quantity = 1
            name = line
        
        item_found = INVENTORY_BY_NAME.get(name.lower())

        if item_found:
            found = True
            price = item_found.price
        else:
            found = False
            price = DEFAULT_ITEM_PRICE
        
        total_price = price * quantity

        response_items.append(GroceryItemResponse(
            name=name,
            quantity=quantity,
            price=price,
            total_price=total_price,
            found=found
        ))


    return EstimateResponse(
        items= response_items,
        item_count= len(response_items),
        estimated_total= sum(item.total_price for item in response_items),
    )
