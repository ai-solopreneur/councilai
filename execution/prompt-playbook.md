# Prompt Execution Playbook

## Purpose
Defines how agents are invoked, sequenced, and coordinated.

---

## Standard Flow
1. Discovery Agent
2. PRD Agent
3. Architecture Agent
4. Compliance Agent
5. Testing Agent
6. Council Debate (if needed)
7. Release Governance Agent

---

## Execution Rules
- One agent per task
- Immutable outputs per phase
- Council required for conflicts
- No skipping stages

---

## Reusability
This playbook is stack-agnostic and cloud-agnostic.
