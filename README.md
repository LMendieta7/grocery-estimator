# Grocery Estimator

FastAPI + React grocery cost estimator with a repository layer that can run from memory or PostgreSQL.

## Backend

Install dependencies:

```bash
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
```

Run with the default in-memory inventory:

```bash
python -m uvicorn backend.app.main:app --reload
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## PostgreSQL

Start Postgres:

```bash
docker compose up -d postgres
```

Create tables and seed inventory:

```bash
source .venv/bin/activate
python -m backend.app.db.seed
```

Run the API using PostgreSQL:

```bash
GROCERY_REPOSITORY_BACKEND=postgres python -m uvicorn backend.app.main:app --reload
```

Default database URL:

```text
postgresql+psycopg://grocery_user:grocery_password@localhost:5432/grocery_app
```

Override it with:

```bash
GROCERY_DATABASE_URL="postgresql+psycopg://user:password@host:5432/database"
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://127.0.0.1:5173
```
