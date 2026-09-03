# AI_ARCHITECTURE.md

## Principle

AI/LLM functionality is isolated from the rest of the application behind a
provider abstraction. No raw LLM API calls happen outside `app/ai/`.

## Planned Structure

```
backend/app/ai/
├── provider/
│   ├── base.py           ← abstract interface all providers implement
│   └── anthropic_provider.py
├── resume_analyzer.py
├── skill_extractor.py
├── job_matcher.py
├── career_advisor.py
├── resume_optimizer.py
└── interview_agent.py
```

## Structured Outputs

AI responses that need structured data are validated against Pydantic
schemas before use — raw model output is never trusted as-is. Example shape
for resume analysis:

```
ResumeAnalysis
├── summary
├── skills
├── experience
├── education
├── projects
├── strengths
├── weaknesses
├── missing_information
└── recommendations
```

## Failure Handling (to implement alongside the first AI feature)

- Invalid/unparseable model output → retry once, then surface a clear error
- API errors / timeouts / rate limits → retried with backoff where sensible,
  otherwise surfaced to the caller
- Provider failures → isolated to the `ai/` layer, don't crash unrelated
  request handling

## Retrieval, Not Dump

The AI career assistant retrieves relevant context (resume, skills,
experience, relevant docs) rather than sending the entire user record to
the LLM on every turn. The retrieval strategy will be documented here once
implemented.

## Current State

Not implemented yet. No AI features exist. This file will be filled in with
the actual provider choice, retrieval strategy, and prompt structure as
those decisions are made (see `DECISIONS.md`).
