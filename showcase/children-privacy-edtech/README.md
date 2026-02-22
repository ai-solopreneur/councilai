# Showcase: Children's EdTech App (Privacy-First)

This showcase focuses on the heavy compliance requirements for EdTech products targeting minors, emphasizing COPPA and FERPA regulations.

## 💼 Project Context
- **Goal**: An interactive learning platform for children aged 6-12.
- **Key Challenges**: Child privacy protection, parental consent management, data minimization.
- **AI Utility**: Personalized tutoring bots that must strictly adhere to safety and privacy constraints.

## 🛡️ Governance Trail

### 📌 [Discovery](discovery.md)
Identifies children as the most vulnerable stakeholder group. Flags "Unauthorized Data Collection" and "Inappropriate AI Content" as critical risks.

### 📋 [PRD](prd.md)
Mandates features like verifiable parental consent, no third-party tracking, and highly filtered AI responses.

### 🏗️ [Architecture](architecture.md)
Designs a system with strict backend isolation for child data and real-time safety guardrails for AI-generated content.

### ⚖️ [Compliance](compliance.md)
A robust control register mapping every feature to COPPA (Children's Online Privacy Protection Act) requirements.

### 🧪 [Testing](testing.md)
Focuses on "Broken Access Control" testing to ensure parents cannot see other children's data and "Jailbreak" testing for the tutoring bot.
