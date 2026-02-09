# CouncilAI Execution Runner – Specification

## Purpose
The CouncilAI Runner executes agent prompts in a controlled, auditable,
and deterministic manner.

It is responsible for execution — not decision-making.

---

## Responsibilities
- Load agent prompt definitions
- Inject project artifacts as context
- Invoke an LLM
- Persist outputs as versioned files
- Validate outputs against rules
- Halt execution on violations

---

## Non-Responsibilities
The Runner MUST NOT:
- Make product decisions
- Override council outcomes
- Skip required stages
- Modify artifacts without traceability
- Act autonomously without human trigger

---

## Execution Contract

Each run must declare:
- Agent name
- Input artifacts
- Output artifact path
- Validation rules
- Escalation conditions

---

## Failure Handling
Execution MUST stop when:
- Output fails validation
- Required artifacts are missing
- Compliance escalation is triggered
- Council approval is required

Failures must be explicit and logged.
