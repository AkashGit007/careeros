=========================
CAREEROS HANDOFF
=========================

CURRENT PROJECT STATE
Repository initialized from scratch. Docs framework, backend skeleton
(FastAPI + health check + DB wiring), no features yet.

CURRENT MILESTONE
Authentication (register, login, JWT)

LAST COMPLETED TASK
Project initialization (repo structure, docs, backend skeleton)

CURRENT TASK
None in progress — ready to start Authentication.

NEXT TASK
Implement `User` model + migration, then `/api/auth/register` and
`/api/auth/login`. See `NEXT_STEPS.md` for full detail and acceptance
criteria.

KNOWN BUGS
None (nothing implemented yet)

IMPORTANT FILES
- backend/app/main.py
- backend/app/core/config.py
- backend/app/db/base.py
- docs/NEXT_STEPS.md

IMPORTANT ARCHITECTURAL DECISIONS
See docs/DECISIONS.md — FastAPI/PostgreSQL/SQLAlchemy/Alembic backend,
Next.js/TypeScript frontend, Anthropic Claude behind a provider
abstraction.

REQUIRED ENVIRONMENT VARIABLES
See .env.example at repo root (DATABASE_URL, SECRET_KEY, LLM_API_KEY, etc).
No real values recorded here — never put secrets in this file.

RUN COMMANDS
cd backend && uvicorn app.main:app --reload

TEST COMMANDS
cd backend && pytest
(no tests exist yet)
