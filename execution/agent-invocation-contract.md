# Agent Invocation Contract

## Invocation Rules
- One agent per execution
- One output artifact per run
- No side effects outside declared outputs

---

## Input Sources
Agents may only read:
- Approved artifacts
- Council decisions
- Explicit configuration files

---

## Output Rules
Agent output must:
- Be deterministic
- Be reviewable
- Be schema-valid
- Contain no hidden instructions

---

## Escalation
If an agent encounters ambiguity, conflict, or risk:
- It MUST escalate
- It MUST NOT guess
