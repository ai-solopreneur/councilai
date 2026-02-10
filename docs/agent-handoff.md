# AI Agent Handoff Guide: Architect -> Builder

CouncilAI is designed to be the **Architect** of your software. It creates the rigorous blueprints (PRDs, Architecture, Compliance) that ensure your product is safe and sound.

To build the software, you can hand these artifacts to a **Builder** (an AI coding agent like Cursor, Windsurf, Devin, or ChatGPT).

---

## ⚡ The Integration Workflow

### 1. Generate the Blueprint
Run CouncilAI to generate your project artifacts:
```bash
council all --project my-project
```

### 2. Provide Context to your Coding Agent
When starting a coding session with your agent, provide the entire project directory as context.

- **In Cursor/Windsurf:** Use `@project-directory` or attach the `projects/my-project/` folder.
- **In ChatGPT/Claude:** Upload all `.md` files from `projects/my-project/`.

### 3. Use the "Architect's Master Instruction"
Copy and paste the following prompt to your coding agent to ensure it follows the CouncilAI governance trail.

---

## 📜 Master Prompt for Coding Agents

> **System Instruction:**
> You are the **Lead Software Engineer (Builder)**. Your task is to implement the project defined in the attached artifacts.
> 
> **Your Source of Truth:**
> 1. `prd.md`: Follow these requirements strictly. Do not add "phantom features."
> 2. `architecture.md`: Adhere to the system design, tech stack, and data models defined here.
> 3. `compliance.md`: You MUST implement all security and privacy controls listed in the Control Register.
> 4. `testing.md`: Ensure your code is testable according to these verification strategies.
> 
> **Your Constraints:**
> - If a requirement in the PRD conflicts with the Architecture, ask me (the Human) for clarification.
> - Do not make "creative" decisions that bypass the compliance controls.
> - Prioritize security and auditability as defined in the governance artifacts.
> 
> **Current Task:**
> [Describe what you want to build now, e.g., "Implement the user authentication flow based on the Architecture spec."]

---

## 🚀 Why This Works
- **No Hallucinations**: The coding agent doesn't have to "guess" your requirements; they are explicitly documented.
- **Compliance by Design**: Since the agent is reading `compliance.md`, it won't "forget" to add encryption or age verification.
- **Clear Accountability**: If the code fails, you can trace it back to whether the Architect (CouncilAI) or the Builder (Coding Agent) missed a detail.
