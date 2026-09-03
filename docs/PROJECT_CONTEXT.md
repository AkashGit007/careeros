# PROJECT_CONTEXT.md

## Product Vision

CareerOS is an AI-powered Career Operating System. It helps a user understand
their career, improve their profile, discover opportunities, identify skill
gaps, prepare for interviews, and receive personalized career guidance.

## Goals

- Build a functional MVP first (see NEXT_STEPS.md for the current milestone),
  then layer in advanced features.
- Every feature must be explainable: how it works, why it was built this way,
  what its limitations are.
- Portfolio-quality: production-reasonable architecture, not a toy demo.

## Main Features (target end-state)

- User management (auth, profile, settings)
- Resume intelligence (upload, parsing, scoring, suggestions, versioning)
- Job intelligence (search, ingestion, matching, missing-skill identification)
- Career intelligence (skill graph, skill-gap analysis, roadmap)
- AI career assistant (retrieval-based, not "dump the whole DB into the prompt")
- Interview intelligence (mock interviews, evaluation, feedback)
- Application tracking
- Dashboard (readiness, matches, skill gaps, progress)

## Technology Stack

### Backend
- Python 3.11+
- FastAPI
- Pydantic (v2) for validation and schemas
- SQLAlchemy (ORM)
- PostgreSQL
- Alembic (migrations)

### Frontend
- Next.js (React) + TypeScript
- Component-based architecture; styling approach TBD when frontend work starts

### AI
- Provider-abstracted LLM client (`backend/app/ai/provider/`)
- Default provider: Anthropic Claude (see `.env.example` for `LLM_PROVIDER`)
- Structured outputs validated with Pydantic schemas — never trust raw LLM
  text as structured data
- Context sent to the LLM is retrieved/relevant, not the entire database

### Infrastructure
- Git / GitHub as the system of record for code and project memory
- Docker introduced once there's enough to containerize meaningfully (not yet)
- Environment variables via `.env` (never committed) / `.env.example` (template)

## Repository Structure

```
careeros/
├── README.md
├── docs/                  ← persistent project memory (read this first)
├── backend/
│   └── app/
│       ├── main.py
│       ├── core/          ← config, security primitives
│       ├── api/           ← route handlers (thin — no business logic)
│       ├── models/        ← SQLAlchemy models
│       ├── schemas/       ← Pydantic request/response schemas
│       ├── services/      ← business logic
│       ├── repositories/  ← DB access
│       ├── ai/            ← LLM provider abstraction + AI features
│       ├── db/            ← session/engine setup
│       └── utils/
└── frontend/              ← Next.js app (not yet scaffolded)
```

Layering:

```
API → Service → Repository → Database
API → AI Service → LLM Provider
```

Business logic stays out of route handlers.

## Coding Conventions

- Type-annotate Python code; use Pydantic models for all API I/O.
- Keep LLM calls behind the `ai/provider/` abstraction — never scatter raw
  API calls through the codebase.
- Validate all model output before using it (schema validation, not just
  "assume it's valid JSON").
- Small, reviewable commits with meaningful messages (see `DECISIONS.md`
  and the Git workflow in the root master prompt).

## Security Principles

- No hard-coded credentials, ever.
- `.env` is never committed; `.env.example` documents variable names only.
- Passwords hashed (not encrypted, not plaintext).
- User-level data isolation — a user can never read another user's data.
- Least privilege for any external integration.

## Database Strategy

Only implement models needed for the current milestone (see
`DATABASE_SCHEMA.md`). Use Alembic migrations for every schema change.

## External Services

None integrated yet. Will be added (and documented here) as needed —
e.g. an LLM provider API, job board APIs, OAuth providers.

## Development Constraints

- Solo developer, using this project as a portfolio piece, working under a
  tight schedule.
- Development happens across multiple AI coding sessions/accounts — nothing
  important may live only in conversation history. It must land in this repo.

## Important Assumptions

- No existing codebase — this project starts from an empty repository as of
  the initialization commit.
- Anthropic Claude is the default LLM provider, but the AI layer is
  provider-abstracted so this can change without touching feature code.
