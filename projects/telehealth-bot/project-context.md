# Telehealth Triage Bot — Project Context

## Product Name
**HealthFirst Triage Bot**

## Problem
Patients calling healthcare providers often wait 20+ minutes to speak with a nurse for basic triage. This creates:
- Poor patient experience
- Wasted clinical staff time on routine questions
- Delayed care for urgent cases
- High operational costs

## Solution
An AI-powered triage bot that:
- Collects patient symptoms via chat interface
- Assesses urgency level (emergency, urgent, routine)
- Routes to appropriate care pathway
- Provides clear next steps
- **Does NOT provide medical advice or diagnosis**

## Users
- **Primary**: Patients seeking initial triage
- **Secondary**: Nurses reviewing bot recommendations
- **Tertiary**: Healthcare administrators monitoring system

## Scope

### In Scope
- Symptom collection via structured questions
- Urgency classification (emergency / urgent / routine)
- Care pathway routing
- HIPAA-compliant data handling
- Audit logging of all interactions
- Human escalation triggers

### Out of Scope
- Medical diagnosis
- Treatment recommendations
- Prescription management
- Direct scheduling (phase 2)
- Integration with EHR systems (phase 2)

## Constraints

### Regulatory
- **HIPAA compliance** (Protected Health Information handling)
- **Medical device classification** (likely Class II - FDA guidance required)
- **State telehealth regulations** (varies by state)

### Technical
- Must integrate with existing patient portal
- Response time < 2 seconds
- 99.9% uptime SLA
- Encrypted data at rest and in transit

### Behavioral Safety
- **MUST refuse to provide medical advice**
- **MUST escalate to human for:**
  - Chest pain, difficulty breathing, severe bleeding
  - Suicidal ideation
  - Pediatric emergencies (< 2 years old)
  - Pregnancy complications
- **MUST clarify** it is not a doctor
- **MUST log** all escalations

## Compliance Needs
- HIPAA (Protected Health Information)
- SOC 2 Type II (data security)
- FDA guidance for clinical decision support software
- State-specific telehealth regulations

## Success Criteria
- 70% of routine cases handled without nurse intervention
- < 5% false negatives (missed urgent cases)
- 90% patient satisfaction score
- Zero HIPAA violations
- 100% audit trail completeness

## Risk Tolerance
**Low** — This is a healthcare application. Safety and compliance are non-negotiable.
