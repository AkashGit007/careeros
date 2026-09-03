# Next Steps

## Current Milestone

Authentication (register, login, JWT auth, user model)

## Current State

Repository is initialized: folder structure, docs, minimal FastAPI app with
a health check endpoint, SQLAlchemy base/session wiring. No auth, no models
beyond scaffolding, no frontend pages yet.

## Remaining

- Define `User` SQLAlchemy model + Alembic migration
- Pydantic schemas: `UserCreate`, `UserRead`, `Token`
- Password hashing (passlib/bcrypt or argon2)
- `POST /api/auth/register`
- `POST /api/auth/login` (returns JWT)
- Auth dependency (`get_current_user`) for protected routes
- Basic tests: register, login, reject bad credentials, protected route
  rejects missing/invalid token

## Relevant Files

- `backend/app/main.py`
- `backend/app/core/config.py`
- `backend/app/db/base.py`
- `backend/app/models/` (new: `user.py`)
- `backend/app/schemas/` (new: `user.py`, `auth.py`)
- `backend/app/api/` (new: `auth.py`)
- `backend/app/services/` (new: `auth_service.py`)
- `backend/app/repositories/` (new: `user_repository.py`)
- `backend/app/core/` (new: `security.py` for hashing/JWT)

## Required Commands

```bash
cd backend
pip install -r requirements.txt
# once DB is running:
alembic upgrade head
uvicorn app.main:app --reload
```

## Next Task

Implement the `User` model + migration, then the register/login endpoints.

## Acceptance Criteria

- User can register with email + password
- Duplicate email registration is rejected with a clear error
- Passwords are hashed, never stored in plaintext
- User can log in and receive a JWT
- Invalid credentials are rejected
- A protected test route rejects requests without a valid token
- Tests exist and pass for the above
- Swagger docs (`/docs`) reflect the new endpoints
- `docs/API_REFERENCE.md` and `docs/DATABASE_SCHEMA.md` updated
