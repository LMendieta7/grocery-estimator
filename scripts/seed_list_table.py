from backend.app.db.models.shopping_list import ShoppingListTable
from backend.app.db.session import SessionLocal
from sqlalchemy import select

def seed_list_table(db):

    default_list = db.scalar(
    select(ShoppingListTable).where(ShoppingListTable.id == 1)
)
    if default_list is not None:
        print("default list already exist")
        return 
    db.add(ShoppingListTable(name="Shopping List"))
    db.commit()
    print("list table seeded")


def main():
    
    with SessionLocal() as db:
        
        seed_list_table(db)
           

if __name__ == "__main__":
    main()
