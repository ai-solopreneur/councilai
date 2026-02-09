# Council Decisions – Telehealth Triage Bot

## Decision 001: AI Autonomy Level
**Issue**: Should the AI be allowed to tell a patient "You are fine" without human review?
**Positions**:
- **Product**: Yes, for efficiency and user speed.
- **Legal/Compliance**: NO. Liability risk is too high.
- **Engineering**: We can implement it, but accuracy isn't 100%.

**Decision**: **Human-in-the-Loop for "Safe" Verdicts**.
- If AI says "Emergency", tell patient immediately.
- If AI says "Self-care", route to Nurse queue for rapid async review before releasing the message.
- **Rationale**: Better to false-alarm an emergency than false-negative a heart attack.

## Decision 002: Cloud Provider Selection
**Issue**: AWS vs Azure vs GCP.
**Decision**: **AWS**.
- **Rationale**: Existing BAA is most mature, and team has deep AWS security expertise. Migrating would introduce unknown risks.
