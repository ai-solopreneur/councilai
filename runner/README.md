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

## Usage

### Run an Agent

```bash
# From project root
council discovery

# This will:
# 1. Read agents/discovery-agent.md
# 2. Call your configured LLM
# 3. Validate the output
# 4. Save to discovery.md
```

### Switch Providers

```bash
# Use OpenAI
export COUNCIL_LLM_PROVIDER=openai
council discovery

# Use Anthropic
export COUNCIL_LLM_PROVIDER=anthropic
council discovery
```
