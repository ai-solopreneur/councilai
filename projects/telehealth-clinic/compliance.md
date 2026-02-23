# Compliance Scope Summary

Applicable Regulations:
- Health Insurance Portability and Accountability Act (HIPAA) for handling and protecting Protected Health Information (PHI)
- AIUC-1 (AI Agent Governance Standard) for AI assistant behavior and operations
- ISO 42001 (AI Management System) for managing AI systems and processes

Jurisdictional Considerations:
- The application will primarily comply with the United States' HIPAA regulations. If the app will be used in other countries or regions, additional local health data protection regulations may apply.

# Data Classification Table

| Data Type | Sensitivity Level | Storage Constraints | Retention Limits | Deletion Requirements |
| --------- | ----------------- | ------------------- | ---------------- | -------------------- |
| Personal Data (User Profile) | High | Encrypted storage, Access control | As long as the user account is active | Deletion upon user account termination |
| Health Data (Medical Records, Consultation history) | High | Encrypted storage, Access control | As specified by HIPAA or local regulations | Deletion upon user request or account termination |
| Financial Data (Billing information) | High | Encrypted storage, PCI-DSS compliance | As long as the user account is active | Deletion upon user account termination |

# Control Register

| Control ID | Description | Regulation Mapping | Enforcement Mechanism | Owner |
| ---------- | ----------- | ------------------ | --------------------- | ----- |
| C1 | User authentication and access control | HIPAA, AIUC-1 | Unique user ID, secure password policies, 2FA | Security Team |
| C2 | Encryption of sensitive data at rest and in transit | HIPAA, AIUC-1, ISO 42001 | Data encryption protocols | DevOps Team |
| C3 | Audit trails and logging | HIPAA, AIUC-1, ISO 42001 | Automated logging and audit trail systems | DevOps Team |
| C4 | Compliance with 'Minimum Necessary' rule | HIPAA | Role-based access control (RBAC) | Security Team |

# Control → Test Mapping

| Control ID | Test Type | Evidence |
| ---------- | --------- | -------- |
| C1 | Automated | Access logs, Test reports |
| C2 | Automated | Encryption validation tests, Security scanning reports |
| C3 | Periodic Audit | Audit reports, Log files |
| C4 | Manual/Automated | RBAC configuration, Access logs |

# Compliance Risks
- Inconsistent internet connectivity in remote areas may impact the integrity and availability of health data.
- Risk of non-compliance with local health data protection regulations in regions outside the United States.

# Council Flags
1. Decision needed on handling compliance with local health data protection regulations if the app is used outside the United States.
2. Discussion required on strategies to mitigate the risk associated with inconsistent internet connectivity in remote areas. 

# AI Behavioral & Ethical Risk Controls

| Identified Risk | Control | Validation Mechanism | Test/Audit Artifact |
| --------------- | ------- | -------------------- | ------------------- |
| Over-reliance on AI without human validation | Regular audits and reviews of AI outputs | Manual review | Audit reports |
| Ambiguous instruction handling | Clear error messages and guidance when inputs are unclear | Manual review, User feedback | Review reports, User feedback logs |

# Conflicting Compliance Resolution
- In case of conflicting compliance requirements, the strictest applicable control shall prevail. For instance, if local regulations in a certain region have stricter data retention requirements than HIPAA, we will follow the local regulations.
- Any exceptions to this rule will require Council approval.
- Business overrides must be documented with compensating controls.