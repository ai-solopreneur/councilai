# PRD – Telehealth Triage Bot

## Core Features
1. **Symptom Intake**: Natural language chat to gather symptoms.
2. **Severity Classification**: Map symptoms to standard triage scales (e.g., ESI).
3. **Provider Routing**: Connect high-risk patients to on-call nurses.
4. **Audit Trail**: Immutable log of all triage decisions.

## Non-Goals
- Prescribing medication.
- Official medical diagnosis.
- handling insurance payments (Phase 2).

## User Flows
- **Patient**: Login -> Describe Symptoms -> Answer Clarifying Qs -> Receive Recommendation.
- **Nurse**: Receive Alert -> Review Chat Transcript -> Video Call Patient.

## Success Metrics
- Triage accuracy (vs human review benchmarks).
- Escalation rate (percentage of chats routed to human).
- Patient trust score (post-chat survey).

## Compliance Requirements
- **Encryption**: All data encrypted at rest and in transit.
- **Access Control**: Role-based access (Patient sees own data, Nurse sees assigned patients).
- **Consent**: Explicit consent for AI interaction at start of chat.
