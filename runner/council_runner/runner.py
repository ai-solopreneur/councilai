from pathlib import Path
from council_runner.llm import call_llm
from council_runner.validation import validate_output

def run_agent(agent: str, project_dir: str = ".", output_dir: str = "."):
    """
    Run a CouncilAI agent with configurable paths.
    
    Args:
        agent: Agent name (e.g., "discovery")
        project_dir: Project directory containing agents/ folder
        output_dir: Directory to write output files
    """
    project_path = Path(project_dir).resolve()
    output_path = Path(output_dir).resolve()
    
    prompt_path = project_path / "agents" / f"{agent}-agent.md"
    output_file = output_path / f"{agent}.md"

    try:
        with open(prompt_path, "r") as f:
            prompt = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Agent definition not found at {prompt_path}")
        return

    print(f"🤖 Invoking {agent} agent...")
    output = call_llm(prompt)

    print(f"🔍 Validating output...")
    validate_output(agent, output)

    with open(output_file, "w") as f:
        f.write(output)

    print(f"✅ {agent} completed successfully. Output saved to {output_file}")
