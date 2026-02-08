# Compliance Control → Test Matrix

## Purpose
Maps regulatory, security, and privacy controls to concrete test cases.

---

## Example Matrix

| Control | Regulation | Risk | Test Type | Owner |
|------|-----------|------|---------|-------|
| Data Encryption | GDPR | High | Security | Testing Agent |
| Access Control | SOC2 | High | Functional | Testing Agent |
| Audit Logging | SOC2 | Medium | Black-box | Testing Agent |
| Consent Capture | GDPR | High | E2E | Compliance Agent |
| Data Retention | GDPR | Medium | Policy | Compliance Agent |

---

## Rules
- Every control MUST have at least one test
- High-risk controls require E2E + audit verification
- No release without matrix validation
