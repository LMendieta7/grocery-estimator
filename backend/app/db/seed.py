from sqlalchemy import select

from backend.app.db.models import GroceryInventoryRecord
from backend.app.db.session import Base, SessionLocal, engine


INITIAL_INVENTORY = [
    {"name": "Milk", "aliases": ["milk"], "unit": "gallon", "unit_price": 4.29, "store": "Walmart"},
    {"name": "Eggs", "aliases": ["eggs"], "unit": "dozen", "unit_price": 3.99, "store": "Walmart"},
    {
        "name": "Bread (White)",
        "aliases": ["bread", "white bread"],
        "unit": "loaf",
        "unit_price": 2.49,
        "store": "Walmart",
    },
    {
        "name": "Chicken Breast",
        "aliases": ["chicken breast"],
        "unit": "lb",
        "unit_price": 4.49,
        "store": "Walmart",
    },
    {"name": "Bananas", "aliases": ["bananas"], "unit": "each", "unit_price": 0.69, "store": "Walmart"},
    {"name": "Rice", "aliases": ["rice"], "unit": "bag", "unit_price": 5.49, "store": "Walmart"},
]


def seed_database() -> None:
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        for item in INITIAL_INVENTORY:
            for alias in item["aliases"]:
                exists = db.scalar(
                    select(GroceryInventoryRecord).where(
                        GroceryInventoryRecord.store == item["store"],
                        GroceryInventoryRecord.lookup_name == alias,
                    )
                )

                if exists:
                    continue

                db.add(
                    GroceryInventoryRecord(
                        name=item["name"],
                        lookup_name=alias,
                        unit=item["unit"],
                        unit_price=item["unit_price"],
                        store=item["store"],
                    )
                )

        db.commit()


if __name__ == "__main__":
    seed_database()
