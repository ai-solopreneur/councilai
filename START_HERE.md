# Welcome to CouncilAI

If you are new here, start with this file.

CouncilAI is a governance-first system for AI-driven software development.
It helps you use AI safely, consistently, and auditably.

---

## Who This Is For
- Solo founders building serious products
- AI startups scaling fast
- Teams in regulated or enterprise environments

---

## How to Use CouncilAI (15-Minute Start)

### Step 1 — Pick a Project
Choose a real project you want to build or improve.

Example:
- SaaS product
- Internal tool
- Regulated application
- AI-powered service

---

### Step 2 — Run Discovery
Open `agents/discovery-agent.md`.

Answer its questions honestly.
Commit the resulting `discovery.md`.

---

### Step 3 — Continue the Flow
Follow the execution order:
1. Discovery
2. PRD
3. Architecture
4. Compliance
5. Testing
6. Council Review

Each step produces a versioned artifact.

---

## How CouncilAI Flows

CouncilAI does not infer intent. **You declare it once, and the system enforces it.**

### Artifact-Driven Execution

1. You declare your product in `projects/<project-name>/project-context.md`
2. Agents read this context and previous artifacts
3. Each agent produces one artifact
4. The next agent reads that artifact
5. No hidden state, no assumptions

### Learn More

- **Agent Flow:** See [How Agents Build on Each Other](README.md#how-agents-build-on-each-other) in the README
- **Full Example:** Follow the [Telehealth Bot Walkthrough](docs/walkthrough-telehealth-bot.md)

---

You now have an AI system that behaves like a professional engineering org.
