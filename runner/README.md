# CouncilAI Runner (MVP)

The CouncilAI Runner executes a single agent in a controlled,
deterministic, and auditable manner.

## What This Is
- A governed execution engine
- A bridge between protocols and automation

## What This Is Not
- An autonomous AI
- A code generator
- A workflow engine

## Configuration

### 1. Install Dependencies

```bash
cd runner
pip install -e .
```

> [!TIP]
> If you get `zsh: command not found: council`, it means your virtual environment is not activated or the package is not installed. 
> Run: `source test_env/bin/activate` (or your venv's activation script) from the project root.


### 2. Set Up API Keys

Create a `.env` file in the `runner/` directory:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```bash
# Choose your provider
COUNCIL_LLM_PROVIDER=openai  # or "anthropic"

# OpenAI
OPENAI_API_KEY=sk-...
COUNCIL_OPENAI_MODEL=gpt-4  # optional, defaults to gpt-4

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...
COUNCIL_ANTHROPIC_MODEL=claude-3-5-sonnet-20241022  # optional
```

## Quick Start: New Application

Follow these steps in order to build a new application with CouncilAI:

### Step 1: Initialize Your Project

You can now initialize a project from a simple idea. CouncilAI will generate a structured `project-context.md` for you.

```bash
# Initialize project with a brief idea
council init "Marketplace for locally sourced vegetables" --project fresh-market
```

This creates `projects/fresh-market/project-context.md`. Edit this file if you need to refine the product vision.

### Step 2: Run the Entire Lifecycle (Recommended)

Instead of running agents one-by-one, you can run the full CouncilAI lifecycle in a single command:

```bash
# Run all agents from discovery to release-governance
council all --project fresh-market
```

**What happens:**
1. Runs `discovery`, `prd`, `architecture`, `compliance`, `testing`.
2. Attempts to run `release-governance`.
3. If you haven't reviewed artifacts and created `council-decisions.md`, the final step will show as **BLOCKED**.

---

## Detailed Agent Flow (Step-by-Step)

### Step 2: Run Discovery

```bash
council discovery --project my-app
```

This creates `projects/my-app/discovery.md` with stakeholder analysis and compliance mapping.

### Step 3: Run PRD

```bash
council prd --project my-app
```

This creates `projects/my-app/prd.md` with product requirements based on discovery.

### Step 4: Run Architecture

```bash
council architecture --project my-app
```

This creates `projects/my-app/architecture.md` with system design.

### Step 5: Run Compliance

```bash
council compliance --project my-app
```

This creates `projects/my-app/compliance.md` with compliance controls.

### Step 6: Run Testing Strategy

```bash
council testing --project my-app
```

This creates `projects/my-app/testing-strategy.md` with test plan.

### Step 7: Review All Artifacts

You now have a complete set of governance artifacts:
- `project-context.md` — Product declaration
- `discovery.md` — Stakeholder analysis
- `prd.md` — Product requirements
- `architecture.md` — System design
- `compliance.md` — Compliance controls
- `testing-strategy.md` — Test strategy

**Next:** Convene a council review for high-risk decisions.

---

## Usage Reference

### Project-Scoped Execution (Recommended)

Use `--project` to scope execution to a specific project:

```bash
# Run any agent for a specific project
council <agent> --project <project-name>

# Examples:
council discovery --project telehealth-bot
council prd --project my-saas
council architecture --project internal-tool
```

**Requirements:**
- Project directory must exist: `projects/<project-name>/`
- Project context must exist: `projects/<project-name>/project-context.md`

**See:** [Telehealth Bot Walkthrough](../docs/walkthrough-telehealth-bot.md) for a complete example.

### Custom Paths (Advanced)

For advanced use cases, specify custom directories:

```bash
# Specify custom project directory
council discovery --project-dir /path/to/project

# Specify custom output directory
council discovery --output-dir /path/to/output

# Use both
council discovery --project-dir /path/to/project --output-dir /tmp/artifacts
```

**Note:** `--project` and `--project-dir`/`--output-dir` are mutually exclusive.

### Switch Providers

```bash
# Use OpenAI
export COUNCIL_LLM_PROVIDER=openai
council discovery

# Use Anthropic
export COUNCIL_LLM_PROVIDER=anthropic
council discovery
```

## Testing

Run the test suite:

```bash
cd runner
pytest tests/ -v
```
