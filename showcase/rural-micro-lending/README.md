# Showcase: Rural Micro-lending App (FinTech)

This showcase demonstrates how CouncilAI governs high-risk FinTech applications, specifically focusing on KYC (Know Your Customer) and credit risk assessment for rural empowerment.

## 💼 Project Context
- **Goal**: Provide micro-loans (INR 5k - 50k) to farmers in rural India.
- **Key Challenges**: Lack of formal credit history, high operational overhead, regulatory compliance (RBI guidelines).
- **AI Utility**: Extracting data from low-quality ID photos and assessing risk via alternative data points.

## 🛡️ Governance Trail

### 📌 [Discovery](discovery.md)
Identifies stakeholders including rural borrowers, field agents, and NBFC partners. Lists "Identity Fraud" and "Over-indebtedness" as primary risks.

### 📋 [PRD](prd.md)
Defines the loan application flow, emphasizing offline-first capabilities and automated KYC verification.

### 🏗️ [Architecture](architecture.md)
Designs a system with a light mobile frontend, a centralized credit scoring engine, and encrypted artifact storage for auditability.

### ⚖️ [Compliance](compliance.md)
Maps the system to RBI's "Guidelines on Digital Lending," focusing on data sovereignty and transparency.

### 🧪 [Testing](testing.md)
Ensures extreme reliability in low-bandwidth scenarios and verifies the accuracy of the KYC OCR engine.
