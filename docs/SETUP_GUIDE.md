# SETUP_GUIDE.md

## Prerequisites

- Python 3.11+
- PostgreSQL (local install or Docker — Docker Compose not set up yet)
- Node.js (once frontend work starts)

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp ../.env.example ../.env     # then fill in real values in .env
# create a local Postgres DB matching DATABASE_URL in .env

uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for Swagger once endpoints exist.
Visit `http://localhost:8000/health` to confirm the app is running.

## Frontend

Not scaffolded yet. Will be added when frontend work begins (after core
backend milestones, per the project priority order in `PROJECT_CONTEXT.md`).

## Environment Variables

See `.env.example` at the repo root. Never commit `.env`.

## Running Tests

```bash
cd backend
pytest
```

(No tests exist yet — this will be accurate once the auth milestone lands.)
