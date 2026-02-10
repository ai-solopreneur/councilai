# Quick Start - CouncilAI Runner

## Option 1: Using Virtual Environment (Recommended)

```bash
# From project root
cd /Users/suparnbector/Desktop/CouncilAI

# Activate the test environment
source test_env/bin/activate

# Verify installation
council --help

# Run an agent
council discovery
```

## Option 2: Direct Python Execution

If you don't want to activate the virtual environment:

```bash
# From project root
cd /Users/suparnbector/Desktop/CouncilAI

# Run using Python module
python3 -m council_runner.cli discovery
```

## Option 3: Install Globally

```bash
# From project root
cd /Users/suparnbector/Desktop/CouncilAI/runner

# Install to user site-packages
pip3 install --user -e .

# Then you can use 'council' from anywhere
council discovery
```

## Setting Up Your API Key

1. Edit `runner/.env`:
   ```bash
   nano runner/.env
   ```

2. Add your API key:
   ```
   COUNCIL_LLM_PROVIDER=openai
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

3. Save and exit (Ctrl+X, then Y, then Enter)
