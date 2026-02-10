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

## Prerequisites (Must Do First)

Before you can run CouncilAI agents, you must set up the environment:

1. **Activate Virtual Env**: `source test_env/bin/activate`
2. **Setup LLM Config**: Ensure `runner/.env` has your API keys.
3. **Verify Installation**: Run `council --help` to ensure the CLI is available.

See the [Root README](README.md#🚀-quick-start-installation) for full setup instructions.

---

## How to Use CouncilAI (15-Minute Start)

### Step 1: Initialize Your Project

CouncilAI uses a "declarative" model. You don't tell the AI how to code; you declare what you are building and why.

```bash
# Initialize project with a brief idea
council init "Medical triage chatbot for remote areas" --project med-bot
```

This creates a `projects/med-bot/project-context.md` file. Review this file to ensure it captures your vision correctly.

### Step 2: Run the Full Lifecycle

Now, execute the entire CouncilAI sequence in one pass. This will generate your Discovery, PRD, Architecture, Compliance, and Testing strategies.

```bash
# Run the full agent lifecycle
council all --project med-bot
```

**Why this matters:**
This command ensures that no step is skipped and that every artifact (like your PRD) is built on top of the previous one (like Discovery). If a compliance gate is triggered (e.g., medical advice safety), the system will flag it for your review.

---

## 🛠️ After Running Agents

Once the agents complete, you will find a full audit trail in `projects/med-bot/`:

- `discovery.md`: Stakeholders & Risks
- `prd.md`: Product Requirements
- `architecture.md`: System Design
- `compliance.md`: Control Register
- `testing.md`: Verification Strategy

**Final Gate:** Review the artifacts and sign your **Council Decision** in `council-decisions.md`. Only then is your project "Release Ready".

---

## 📚 Learn More
- [How Agents Work Together](README.md#how-agents-build-on-each-other)
- [Telehealth Bot Walkthrough](docs/walkthrough-telehealth-bot.md)
- [Runner Technical Guide](runner/README.md)
