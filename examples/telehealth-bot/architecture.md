# Architecture – Telehealth Triage Bot

## System Context
- **Mobile App**: React Native (Secure Secure Storage).
- **API Gateway**: Mutual TLS (mTLS) required.
- **Triage Engine**: Stateless AI service (No PHI retention in inference logs).
- **Database**: PostgreSQL with row-level encryption.

## Decision 001: Zero-Knowledge AI
- The AI model processes anonymized tokens.
- PII/PHI is stripped at the gateway and re-attached only for the client and nurse dashboard.

## Security Architecture
- **Identity**: OAuth2 + MFA (mandatory).
- **Audit**: Write-once-read-many (WORM) storage for audit logs.
- **Networking**: Private VPC, no public internet access for DB.

## Data Flow
1. User sends message (Encrypted).
2. Gateway decrypts, strips PII, forwards to AI.
3. AI returns triage classification.
4. Gateway re-attaches context, logs decision, returns to User.
