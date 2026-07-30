# Smart Grocery

Smart Grocery is a small SaaS grocery-list application for quickly building
lists, organizing items, and tracking shopping progress.

The application is being built as a focused learning project first, with a
data model that can later support user accounts and shared lists. The build
plan lives in
[docs/smart-grocery-requirements.md](docs/smart-grocery-requirements.md).

## Product Direction

Smart Grocery will use:

- A shared system product catalog that users can search but not modify.
- Shopping-list items that copy catalog defaults and can be edited without
  changing the original product.
- Optional prices and images on shopping-list items.
- Future per-user product preferences for remembered prices, images, and
  default units. Product names do not belong in preferences.
- Future personal products that users can create, reuse, rename, and delete.
- Future list membership so users can share selected shopping lists.

The initial version remains simple and does not require authentication.
Authentication, user ownership, and sharing will be added when the core
shopping-list workflow is complete.

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

## Current Structure

```text
backend/app/
├── core/                 # configuration, database, dependencies
├── products/             # router, services, models, schemas
├── shopping_lists/       # router, services, models, schemas
├── categories/           # category database model used by products
└── main.py               # creates FastAPI app and connects feature routers
```

## SaaS Data Direction

The shared product catalog provides reusable defaults. When a product is
added, its name and category are copied into the shopping-list item:

- Catalog changes do not automatically rewrite existing list items.
- List-item copies can later be edited without changing the original product.
- Estimated prices are optional list-item values. Shared catalog products do
  not store personal prices. The UI shows a total only when at least one list
  item has a price.
- Images will be optional list-item values rather than personal data stored
  on shared catalog products.
- List-item quantities support decimals and use a validated unit such as
  `each`, `pack`, `lb`, `kg`, or `L`.

When users are added, they should be able to:

- Search the original shared catalog.
- Create personal product suggestions.
- Reuse their custom products on other lists.
- Rename or remove their personal products.
- Remove a shopping-list item without deleting its catalog entry.
- Never modify or delete shared system products.

Future personal products can belong to a user, while shared system products
have no user owner. Search results can then combine the shared catalog with
the current user's personal products. If a list-item name differs from its
source product name, the backend can create or reuse a user-owned product with
that name. An unchanged name keeps the original product and does not create a
personal duplicate.
