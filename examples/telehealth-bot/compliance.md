# Compliance – Telehealth Triage Bot

## Control Matrix (HIPAA & GDPR)

| Control ID | Requirement | Implementation | Owner |
|------------|-------------|----------------|-------|
| GOV-001 | Business Associate Agreement (BAA) | Signed with all cloud providers | Legal |
| SEC-001 | Encryption at Rest | AES-256 for DB volumes | Tech Lead |
| SEC-002 | Encryption in Transit | TLS 1.3 only (no downgrades) | Tech Lead |
| PRIV-001 | Right to be Forgotten | Automated script to wipe PII upon request | Data Officer |
| ACC-001 | Minimum Necessary Access | RBAC policies strictly enforced | Security Eng |

## Audit Strategy
- Quarterly 3rd-party penetration testing.
- Weekly automated vulnerability scans.
- Real-time alerting for any unauthorized access attempt.
