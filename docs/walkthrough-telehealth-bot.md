# Walkthrough: Building a Telehealth Triage Bot with CouncilAI

## Introduction

This walkthrough demonstrates how to use CouncilAI to build a **HIPAA-compliant telehealth triage bot** from concept to deployment-ready artifacts.

**What we're building:**  
HealthFirst Triage Bot — an AI-powered system that collects patient symptoms, assesses urgency, and routes to appropriate care pathways.

**Why this example:**  
- High-stakes regulated environment (HIPAA)
- Clear compliance requirements
- Demonstrates CouncilAI's governance value
- Real-world relevance for healthcare and enterprise teams

**Who this is for:**  
- Solo founders building regulated products
- Healthcare startups
- Enterprise teams in compliance-heavy industries
- Anyone needing audit-ready AI development

---

## Step 0: Declare the Product

Before running any agents, you must **declare your project scope** in `project-context.md`.

### Create the Project

```bash
mkdir -p projects/telehealth-bot
```

### Write `projects/telehealth-bot/project-context.md`

This file defines:
- **Problem** — What you're solving
- **Users** — Who will use it
- **Scope** — What's in/out
- **Constraints** — Regulatory, technical, behavioral
- **Compliance needs** — HIPAA, FDA, SOC 2
- **Risk tolerance** — Low (healthcare = safety-first)

**Example:**
```markdown
# Telehealth Triage Bot — Project Context

## Problem
Patients wait 20+ minutes for basic triage. We need an AI bot to:
- Collect symptoms
- Assess urgency
- Route to care pathway
- **NOT provide medical advice**

## Compliance Needs
- HIPAA (Protected Health Information)
- FDA guidance (clinical decision support)
- SOC 2 Type II

## Behavioral Safety
- MUST refuse medical advice
- MUST escalate emergencies (chest pain, bleeding, etc.)
- MUST clarify it's not a doctor
```

See the full example: [`projects/telehealth-bot/project-context.md`](file:///Users/suparnbector/Desktop/CouncilAI/projects/telehealth-bot/project-context.md)

---

## Step 1: Run Discovery

The **Discovery Agent** reads your project context and produces a structured discovery document.

### Run the Agent

```bash
council run discovery --project telehealth-bot
```

### What Happens

1. **Reads:**  
   - `agents/discovery-agent.md` (agent prompt)
   - `projects/telehealth-bot/project-context.md` (your input)

2. **LLM processes:**  
   - Identifies stakeholders
   - Maps compliance requirements
   - Flags risks
   - Defines success criteria

3. **Writes:**  
   - `projects/telehealth-bot/discovery.md`

### Why This Matters

Discovery ensures:
- Compliance is identified **before** architecture
- Risks are surfaced early
- All stakeholders are considered
- The team has a shared understanding

---

## Step 2: Run PRD

The **PRD Agent** reads the discovery document and produces a Product Requirements Document.

### Run the Agent

```bash
council run prd --project telehealth-bot
```

### What Happens

1. **Reads:**  
   - `projects/telehealth-bot/discovery.md` (previous output)

2. **LLM processes:**  
   - Defines features
   - Sets non-goals
   - Specifies user flows
   - Links to compliance requirements

3. **Writes:**  
   - `projects/telehealth-bot/prd.md`

### Artifact Chaining

Notice: The PRD agent **only reads approved artifacts** (discovery.md). It doesn't re-read project-context.md or make assumptions. This is governance by design.

---

## Step 3: Architecture → Compliance → Testing

Continue the flow:

### Architecture

```bash
council run architecture --project telehealth-bot
```

**Produces:** `architecture.md`  
**Focus:** System design, data flow, HIPAA-compliant architecture

### Compliance

```bash
council run compliance --project telehealth-bot
```

**Produces:** `compliance.md`  
**Focus:** HIPAA controls, audit logging, encryption requirements

### Testing

```bash
council run testing --project telehealth-bot
```

**Produces:** `testing-strategy.md`  
**Focus:** Safety testing, compliance validation, edge case handling

---

## Step 4: Council Review

At this point, you have:
- `discovery.md`
- `prd.md`
- `architecture.md`
- `compliance.md`
- `testing-strategy.md`

### When Council Review Is Required

The **Council** (human decision-makers) must review:
- **High-risk decisions** — e.g., "Should we store PHI in the cloud?"
- **Compliance-impacting changes** — e.g., "Can we use third-party LLM APIs?"
- **Release readiness** — "Are we ready to deploy to production?"

### How to Run Council Review

1. Gather stakeholders (product, engineering, compliance, legal)
2. Review all artifacts
3. Debate and resolve conflicts
4. Record decisions in `projects/telehealth-bot/council-decisions.md`

**Example Decision:**
```markdown
# Council Decision: PHI Storage

**Date:** 2026-02-10  
**Participants:** CTO, Compliance Officer, Product Lead

**Decision:** Store PHI in AWS with encryption at rest (AES-256) and in transit (TLS 1.3).

**Rationale:** AWS is HIPAA-compliant (BAA signed). Encryption meets regulatory requirements.

**Risks Accepted:** Vendor lock-in, third-party dependency.
```

---

## Final Outcome

After completing the flow, you have **audit-ready artifacts**:

| Artifact | Purpose |
|----------|---------|
| `project-context.md` | Product declaration |
| `discovery.md` | Stakeholder analysis, compliance mapping |
| `prd.md` | Feature requirements, user flows |
| `architecture.md` | System design, data flow |
| `compliance.md` | HIPAA controls, audit strategy |
| `testing-strategy.md` | Safety testing, validation plan |
| `council-decisions.md` | High-risk decisions, rationale |

### Why This Matters

These artifacts provide:
- **Traceability** — Every decision is documented
- **Compliance readiness** — HIPAA auditors can review the full chain
- **Governance** — No hidden state, no assumptions
- **Team alignment** — Everyone works from the same source of truth

---

## Key Takeaways

1. **CouncilAI does not infer intent** — You declare it once in `project-context.md`, and the system enforces it.

2. **Agents don't chat** — They execute a linear flow, reading approved artifacts.

3. **Governance is built-in** — Council review, behavioral safety, and audit trails are first-class features.

4. **Compliance is not an afterthought** — It's baked into every step of the flow.

---

## Next Steps

- **Run this example yourself:**  
  ```bash
  council run discovery --project telehealth-bot
  ```

- **Adapt for your project:**  
  Replace `telehealth-bot` with your product name and update `project-context.md`.

- **Add real LLM integration:**  
  Configure OpenAI or Anthropic in `runner/.env` (see [`runner/README.md`](file:///Users/suparnbector/Desktop/CouncilAI/runner/README.md)).

- **Set up CI/CD gates:**  
  Block PRs without required artifacts (coming soon).
