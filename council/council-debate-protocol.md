# Council Debate Protocol

## Purpose
The Council Debate Protocol governs how multiple AI agents collaborate,
disagree, escalate, and reach binding decisions in an AI-driven SDLC.

Its goal is to ensure:
- Correctness over speed
- Compliance over convenience
- Evidence over assumptions

---

## When the Council Is Triggered

A Council Debate MUST be initiated when:
- Two or more agents produce conflicting outputs
- A compliance control impacts product scope or UX
- A test failure blocks release
- A security or privacy risk is identified
- A release decision is required

---

## Council Members & Voting Power

| Agent | Role | Vote Weight |
|------|------|------------|
| Discovery Agent | User & market truth | 1 |
| PRD Agent | Business intent | 1 |
| Architecture Agent | Technical feasibility | 1 |
| Compliance Agent | Regulatory & risk | 2 |
| Testing Agent | Evidence & quality | 2 |

Compliance and Testing have **override authority**.

---

## Debate Structure (MANDATORY)

Each Council Debate follows this exact sequence:

### 1. Issue Statement
- Clear description of the conflict
- Impacted artifacts
- Decision required

---

### 2. Agent Positions

Each agent must provide:
- Their stance
- Supporting evidence
- Risks if their stance is ignored

No generic opinions allowed.

---

### 3. Conflict Analysis

Council identifies:
- Direct conflicts
- Hidden dependencies
- Compliance implications
- Long-term risks

---

### 4. Decision Options

At least:
- Option A (status quo)
- Option B (change required)
- Option C (hybrid / phased)

Each option must include tradeoffs.

---

### 5. Final Decision

Decision is based on:
- Risk minimization
- Compliance adherence
- Testability
- User impact

---

## Safety & Compliance Deadlock Rule

If agents disagree on:
- Legal compliance
- User safety
- Ethical implications
- Degree of automation

The Council MUST:
1. Default to the safest option
2. Require human decision logging
3. Record rationale in the decision record

No optimization (speed, cost, convenience) may override safety or compliance.


If Compliance or Testing votes “BLOCK,” the decision is blocked.

---

### 6. Decision Record (MANDATORY)

Every debate produces a record:

- Decision ID
- Summary
- Accepted option
- Rejected options
- Rationale
- Conditions (if any)
- Follow-up actions
- Re-review triggers

This record is immutable.

---

## Escalation Rules

Automatic escalation if:
- Compliance risk ≥ High
- Security risk ≥ Medium
- Data privacy affected
- Production release requested

---

## Release Authority

A release is allowed only if:
- No open BLOCK votes
- All critical tests pass
- Compliance controls verified

---

## Anti-Patterns (Forbidden)

- Silent overrides
- “We’ll fix later”
- Ignoring minority objections
- Speed-first decisions

---

## Output Artifacts

Each debate MUST generate:
- Council Decision Record
- Updated artifacts (if required)
- Updated risk register

No undocumented decisions allowed.
