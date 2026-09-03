# DECISIONS.md

Architectural and technical decisions, in chronological order. Append new
entries — don't rewrite history.

---

## 2026-09-03 — Initial stack selection

**Decision:** Python/FastAPI backend, PostgreSQL + SQLAlchemy + Alembic,
Next.js/TypeScript frontend, Anthropic Claude as default LLM provider
behind a provider abstraction.

**Why:**
- FastAPI + Pydantic gives strong request/response validation and free
  OpenAPI docs, which matters for a portfolio project meant to demonstrate
  API design.
- PostgreSQL is a reasonable, explainable default for relational data
  (users, resumes, jobs, applications) with room to add full-text or vector
  search later if needed for matching/retrieval.
- Next.js is a common, well-understood choice for a React frontend with
  good defaults for routing and API integration.
- LLM calls are isolated behind `app/ai/provider/` so the provider can
  change without touching feature code — avoids lock-in and keeps AI
  logic testable/mockable.

**Alternatives considered:** Django (more batteries-included, but FastAPI's
async support and OpenAPI generation fit this project better); a NoSQL
store (rejected — the domain is relational: users have resumes have
versions, jobs have skills, applications reference both).

**Trade-offs accepted:** More setup work up front (migrations, layered
architecture) than a quick script-style app, in exchange for something
that's actually explainable in an interview and reasonably production-like.

---

## 2026-09-03 — Repository started from scratch

**Decision:** No prior codebase existed under the given GitHub URL, so the
project was initialized fresh: folder structure, `docs/` memory files,
minimal FastAPI skeleton, `.gitignore`, `.env.example`.

**Why:** Nothing to inspect or preserve; starting clean avoids carrying
over assumptions from a nonexistent prior implementation.
