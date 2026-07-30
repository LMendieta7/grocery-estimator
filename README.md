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
