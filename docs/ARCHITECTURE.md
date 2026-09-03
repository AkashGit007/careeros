# ARCHITECTURE.md

## Overview

CareerOS follows a layered backend architecture with a clean separation
between the API surface, business logic, data access, and AI functionality.

```
                    CAREEROS
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     PROFILE        RESUME          JOBS
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                CAREER INTELLIGENCE
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
    SKILL GAP       MATCHING       CAREER PATH
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                  AI ASSISTANT
                       │
                       ↓
                INTERVIEW AGENT
                       │
                       ↓
                 CAREER GROWTH
```

## Backend Layering

```
API (FastAPI routes)
  ↓
Service (business logic)
  ↓
Repository (DB access)
  ↓
Database (PostgreSQL via SQLAlchemy)
```

```
API
  ↓
AI Service
  ↓
LLM Provider (abstraction over Anthropic/other providers)
```

Route handlers stay thin: validate input (via Pydantic schema), call a
service, return a response schema. No business logic in `api/`.

## AI Architecture

See `AI_ARCHITECTURE.md` for the full design. Summary: LLM calls are never
made directly from route handlers or services outside `app/ai/`. Everything
goes through `app/ai/provider/base.py`'s abstraction so the provider can be
swapped and calls can be tested/mocked.

## Document Pipeline (Resume Intelligence)

```
Upload → Validation → Storage → Text Extraction → Document Classification
  → Information Extraction → Structured Career Data → Career Memory → AI Retrieval
```

The original uploaded file is preserved; extracted structured data is stored
separately from the raw file.

## Current State

No components implemented yet — this document will be filled in as each
piece is built, and kept in sync with the real implementation (code and
tests are the source of truth if this doc ever drifts).
