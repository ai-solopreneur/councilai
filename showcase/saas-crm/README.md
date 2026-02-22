# Showcase: Modern SaaS CRM (General Utility)

This showcase demonstrates that CouncilAI isn't just for highly regulated industries—it provides immense value for general-purpose SaaS products through architectural consistency and requirements traceability.

## 💼 Project Context
- **Goal**: A multi-tenant CRM for small business owners.
- **Key Challenges**: Multi-tenancy isolation, complex API integrations, user-friendly reporting.
- **AI Utility**: Automated lead scoring and conversation summarization.

## 🛡️ Governance Trail

### 📌 [Discovery](discovery.md)
Focuses on competitor analysis and identifying "System Scalability" as a key long-term risk.

### 📋 [PRD](prd.md)
Standard functional requirements for lead management, task tracking, and email integration.

### 🏗️ [Architecture](architecture.md)
A classic multi-tenant architecture using PostgreSQL row-level security and a React/FastAPI stack.

### ⚖️ [Compliance](compliance.md)
Focuses on "Cyber Hygiene"—ensuring basic security headers, encrypted backups, and MFA are in place.

### 🧪 [Testing](testing.md)
Focuses on integration tests for third-party APIs (Stripe, HubSpot) and multi-tenancy leakage tests.
