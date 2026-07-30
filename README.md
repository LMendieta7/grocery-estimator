# Smart Grocery

Smart Grocery is a modern grocery planning app for building grocery lists, estimating costs, tracking shopping progress, and maintaining a personal grocery catalog.

The current codebase is still a small FastAPI learning skeleton. The agreed product direction and build plan live in [docs/smart-grocery-requirements.md](docs/smart-grocery-requirements.md).

## Backend

Install dependencies:

```bash
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
```

Run the API:

```bash
python -m uvicorn backend.app.main:app --reload
```

API docs:

```text
http://127.0.0.1:8000/docs
```

Test in Swagger with:

```json
{
  "grocery_text": "milk\nbread\neggs"
}
```

## Current Structure

```text
backend/app/
├── core/                 # configuration, database, dependencies, security, exceptions
├── products/             # router, services, models, schemas
├── shopping_lists/       # router, services, models, schemas
├── categories/           # category database model used by products
└── main.py               # creates FastAPI app and connects feature routers
```

## Future Personal Products

The shared product catalog provides reusable defaults. When a product is
added, its name, category, and estimated price are copied into the
shopping-list item:

- Catalog changes do not automatically rewrite existing list items.
- List-item copies can later be edited without changing the original product.

When users are added, they should be able to:

- Search the original shared catalog.
- Create personal product suggestions.
- Reuse their custom products on other lists.
- Rename or remove their personal products.
- Remove a shopping-list item without deleting its catalog entry.
- Never modify or delete shared system products.

Future personal products can belong to a user, while shared system products
have no user owner. Search results can then combine the shared catalog with
the current user's personal products.
