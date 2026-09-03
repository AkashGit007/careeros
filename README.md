# CareerOS

An AI-powered Career Operating System — resume intelligence, job matching,
skill-gap analysis, an AI career assistant, and interview prep, in one platform.

## Status

🟡 **Project initialized.** No features implemented yet. See `docs/DEVELOPMENT_STATUS.md`.

## For a new developer / new AI session

Start here, in order:

1. `docs/PROJECT_CONTEXT.md` — what this is and why
2. `docs/ARCHITECTURE.md` — how it's structured
3. `docs/DEVELOPMENT_STATUS.md` — what's done / in progress / not started
4. `docs/NEXT_STEPS.md` — the concrete next task
5. `docs/HANDOFF.md` — the last session's handoff notes

**The repository, not any conversation history, is the source of truth for this project.**

## Quickstart

See `docs/SETUP_GUIDE.md`.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL, Alembic
- **Frontend:** Next.js, TypeScript
- **AI:** LLM provider abstraction (Anthropic Claude by default), structured outputs via Pydantic
- **Infra:** Docker (added once useful), GitHub, environment-based config

See `docs/DECISIONS.md` for why.
