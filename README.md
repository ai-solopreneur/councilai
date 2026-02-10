# CouncilAI – AI-Driven SDLC Meta-System

## Overview
CouncilAI is a governance-first, compliance-aware, multi-agent AI system designed
to execute the full Software Development Lifecycle (SDLC) with enterprise-grade rigor.

This is not a code generator.  
This is not autonomous AI.

CouncilAI is an **AI operating model** that enables humans to **orchestrate AI agents safely, transparently, and with full accountability**.

It enforces:
- Human-in-the-loop decision making
- Behavioral safety constraints for AI agents
- Regulatory and compliance readiness
- Auditability and traceability by design

---

## Core Principles
- Single-Responsibility AI Agents
- Humans as orchestrators, not code typists
- Safety over speed
- Human oversight by default
- Evidence-based decision making
- Compliance-first architecture
- Test-driven validation
- Explicit governance over autonomy
- AI agents must ask, not assume

---

## System Components

### Agents
CouncilAI is composed of specialized AI agents, each with clearly defined roles,
authority boundaries, and behavioral constraints:

- Discovery Agent
- PRD Agent
- Architecture Agent
- Compliance Agent
- Testing Agent
- Release & Governance Agent

Agents generate **proposals**, not final decisions.

All irreversible, high-risk, or compliance-impacting actions require governance
review and human approval.

---

## How Agents Build on Each Other

CouncilAI agents execute in a **linear, artifact-driven flow**. Each agent reads approved artifacts from previous steps and produces a new artifact that becomes input for the next agent.

### The Flow

```
project-context.md
      ↓
discovery.md
      ↓
prd.md
      ↓
architecture.md
      ↓
compliance.md
      ↓
testing-strategy.md
      ↓
council-review
```

### Key Principles

1. **Agents Don't Chat** — Each agent has a single, well-defined responsibility. There is no back-and-forth conversation.

2. **Artifacts Are Truth** — Agents only read approved, versioned artifacts. No hidden state, no inference.

3. **Each Output Becomes Next Input** — The discovery agent's output (`discovery.md`) becomes input for the PRD agent. The PRD agent's output (`prd.md`) becomes input for the architecture agent. And so on.

4. **No Skipping Steps** — Skipping steps breaks governance. If you skip discovery and jump to architecture, you lose traceability and compliance readiness.

### When Council Review Is Required

The **Council** (human decision-makers) must review and approve:
- High-risk architectural decisions
- Compliance-impacting changes
- Release decisions
- Escalations flagged by agents

Council decisions are recorded in `council-decisions.md` and become part of the audit trail.

---

Each agent operates under a mandatory **Behavioral Safety Contract**.

---

### Council
The Council is a structured debate and resolution protocol that governs agent output.

It:
- Resolves cross-agent conflicts
- Enforces safety and compliance constraints
- Applies regulatory veto power when required
- Records architectural, product, and risk decisions
- Governs release readiness
- Defaults to the safest option during disagreement

The Council acts as the **decision boundary between AI autonomy and human authority**.

---

### Safety & Behavioral Governance
CouncilAI explicitly governs **AI behavior**, not just SDLC process flow.

All agents are bound by a Behavioral Safety Contract that enforces:
- Clarification over assumption
- Human approval for irreversible actions
- Rejection of unsafe, misleading, or deceptive outputs
- Escalation on ambiguity, conflict, or compliance risk

See:
- `governance/behavioral-safety-contract.md`

Violations block release and require council resolution.

---

### Compliance & Risk
CouncilAI treats compliance as a continuous system property, not a phase.

It includes:
- Compliance Control → Test Matrix
- Central Risk Register with ownership and lifecycle
- Ethical and AI-behavioral risk tracking
- Escalation and deadlock resolution rules
- Audit-ready artifacts suitable for regulated environments

Compliance conflicts default to the strictest applicable control unless explicitly
overridden by council decision with documented rationale.

---

### Execution Model
CouncilAI enforces a non-skippable SDLC flow:

1. Discovery
2. Product Definition
3. Architecture
4. Compliance Analysis
5. Testing & Verification
6. Council Debate (if required)
7. Release Governance

Each stage produces verifiable artifacts.
Agent work may span **multiple sessions or days**, with state preserved through
versioned documents and decision records.

---

## How CouncilAI Is Used

1. **Manual Mode**  
   Humans execute the agents by following the protocols directly.

2. **AI-Assisted Mode**  
   Each agent prompt is executed via an LLM, with outputs committed as artifacts.

3. **Automated Mode (Planned)**  
   Runners, CI/CD gates, and dashboards will enforce CouncilAI automatically.

---

## What This Repository Is (and Is Not)

**CouncilAI is NOT:**
- A code generator
- A chatbot workflow
- A replacement for engineers
- An uncontrolled autonomous agent system

**CouncilAI IS:**
- A governance layer for AI-driven development
- A compliance-first SDLC operating system
- A trust framework for agentic software development
- A foundation for regulated, enterprise-grade systems

---

## Who Should Use This
- Solo founders building serious AI products
- AI-first startups preparing for enterprise adoption
- Enterprise innovation teams
- Regulated industries (FinTech, HealthTech, GovTech)

---

## What Makes CouncilAI Different
CouncilAI governs **decision-making**, not just task execution.

It:
- Treats AI output as advisory, not authoritative
- Preserves human accountability
- Prevents unsafe autonomy by design
- Creates a durable audit trail for AI-driven development

CouncilAI is not an AI assistant.  
It is an **AI governance system**.

---

## Roadmap
- Execution Runner (CLI)
- Compliance & Safety CI/CD Gates
- Council Dashboard
- Security Agent (STRIDE / SAST / Supply Chain)
- Enterprise Policy Packs

---

## Status
CouncilAI is currently in **Protocol v1.0 (Specification Complete)**.

Execution tooling is intentionally decoupled from governance to preserve trust,
auditability, and correctness.

---

## License & Usage
This repository represents a reusable AI-driven SDLC framework.

Licensing, commercialization, and execution layers can be added without modifying
the core governance model.
