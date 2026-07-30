from sqlalchemy import select

from backend.app.core.database import SessionLocal
from backend.app.shopping_lists.models import ShoppingListTable


def seed_list_table(db):
    default_list = db.scalar(
        select(ShoppingListTable).where(
            ShoppingListTable.name == "Shopping List"
        )
    )
    if default_list is not None:
        print("Default shopping list already exists.")
        return

    db.add(ShoppingListTable(name="Shopping List"))
    print("Default shopping list seeded.")


def main():
    with SessionLocal() as db:
        seed_list_table(db)
        db.commit()


if __name__ == "__main__":
    main()
