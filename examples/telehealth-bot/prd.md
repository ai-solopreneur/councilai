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

## Safety Requirements
> [!IMPORTANT]
> This product identifies as a "High Risk" Medical Device (SaMD) under FDA guidance.

All agents working on this project must strictly adhere to the [CouncilAI Behavioral Safety Contract](../../governance/behavioral-safety-contract.md).

### Mandatory Behaviors
1. **Refusal to Diagnose**: The system SHALL NOT output a disease name as a fact.
2. **Escalation**: Any input matching "chest pain", "difficulty breathing", or "severe bleeding" triggers immediate hard-stop and 911 prompt.
3. **Traceability**: Every AI response must include a session ID in the metadata for audit.
