import json
from pathlib import Path
from sqlalchemy import select
from backend.app.db.models.category import CategoryTable
from backend.app.db.models.product import ProductTable
from backend.app.db.session import SessionLocal

SCRIPTS_DIR = Path(__file__).resolve().parent

DATA_DIR = SCRIPTS_DIR / "data"
CATEGORIES_PATH = DATA_DIR / "categories.json"
PRODUCTS_PATH = DATA_DIR / "products.json"


def load_json(path: Path):
    with path.open() as seed_file:
        return json.load(seed_file)


def seed_categories(db, categories):
    category_map = {
        category.name: category
        for category in db.scalars(select(CategoryTable)).all()
    }

    for category_data in categories:
        name = category_data["name"]
        if name not in category_map:
            category = CategoryTable(name=name)
            db.add(category)
            category_map[name] = category

    db.flush()

    return category_map


def seed_products(db, products, category_map):
    product_names = {
        name
        for name in db.scalars(select(ProductTable.name)).all()
    }

    for product_data in products:
        name = product_data["name"]
        if name in product_names:
            continue

        category_name = product_data["category"]
        category = category_map[category_name]

        db.add(
            ProductTable(
                name=name,
                category_id=category.id,
                image_url=product_data.get("image_url"),
                notes=product_data.get("notes"),
            )
        )


def main():
    categories = load_json(CATEGORIES_PATH)
    products = load_json(PRODUCTS_PATH)

    with SessionLocal() as db:
        category_map = seed_categories(db, categories)
        seed_products(db, products, category_map)
        db.commit()

    print("Seed data loaded.")
 

if __name__ == "__main__":
    main()
