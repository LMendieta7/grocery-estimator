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
backend/app/main.py                       # creates FastAPI app and connects routers
backend/app/api/routes/estimates.py       # HTTP endpoint
backend/app/schemas/estimate.py           # request/response data shapes
backend/app/services/estimate_service.py  # business logic
backend/app/models/grocery_item.py        # internal dataclass model
```
