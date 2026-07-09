from sqlalchemy import select
from backend.app.db.session import SessionLocal
from backend.app.db.models.product import ProductTable
from decimal import Decimal

STARTER_PRODUCTS = [
    ProductTable(
        name="Whole Milk",
        brand="Great Value",
        description="Vitamin D whole milk",
        category="Dairy",
        store="Walmart",
        size="1 gallon",
        current_price=Decimal("4.29"),
    ),
    ProductTable(
        name="Large Eggs",
        brand="Great Value",
        description="Grade A large white eggs",
        category="Dairy",
        store="Walmart",
        size="12 count",
        current_price=Decimal("3.99"),
    ),
    ProductTable(
        name="White Bread",
        brand="Great Value",
        description="Classic white sandwich bread",
        category="Bakery",
        store="Walmart",
        size="20 oz",
        current_price=Decimal("1.88"),
    ),
    ProductTable(
        name="Bananas",
        brand=None,
        description="Fresh bananas",
        category="Produce",
        store="Walmart",
        size="1 lb",
        current_price=Decimal("0.58"),
    ),
    ProductTable(
        name="Gala Apples",
        brand=None,
        description="Fresh gala apples",
        category="Produce",
        store="Walmart",
        size="3 lb bag",
        current_price=Decimal("4.97"),
    ),
    ProductTable(
        name="Chicken Breast",
        brand="Tyson",
        description="Boneless skinless chicken breast",
        category="Meat",
        store="Walmart",
        size="2.5 lb",
        current_price=Decimal("11.98"),
    ),
    ProductTable(
        name="White Rice",
        brand="Mahatma",
        description="Long grain white rice",
        category="Pantry",
        store="Walmart",
        size="5 lb",
        current_price=Decimal("4.98"),
    ),
    ProductTable(
        name="Spaghetti Pasta",
        brand="Great Value",
        description="Dry spaghetti pasta",
        category="Pantry",
        store="Walmart",
        size="16 oz",
        current_price=Decimal("0.98"),
    ),
    ProductTable(
        name="Yellow Onions",
        brand=None,
        description="Fresh yellow onions",
        category="Produce",
        store="Walmart",
        size="3 lb bag",
        current_price=Decimal("2.74"),
    ),
    ProductTable(
        name="Russet Potatoes",
        brand=None,
        description="Fresh russet potatoes",
        category="Produce",
        store="Walmart",
        size="5 lb bag",
        current_price=Decimal("3.47"),
    ),
]

def seed_db():
    db = SessionLocal()
    try:
        item = db.scalars(select(ProductTable).limit(1)).first
        if item is not None:
            print("Product already exist. Skipping seed.")
            return
        
        db.add_all(STARTER_PRODUCTS)
        db.commit()

        print("Seed data inserted.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_db()