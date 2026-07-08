# Grocery Estimator Learning Skeleton

A small FastAPI backend for learning how routes, schemas, services, and models fit together.

This branch is intentionally simple so you can rebuild the app step by step.

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
