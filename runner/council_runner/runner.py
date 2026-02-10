from pathlib import Path
from typing import Optional
from council_runner.llm import call_llm
from council_runner.validation import validate_output

def run_agent(
    agent: str, 
    project: Optional[str] = None,
    project_dir: Optional[str] = None, 
    output_dir: Optional[str] = None
):
    """
    Run a CouncilAI agent with configurable paths.
    
    Args:
        agent: Agent name (e.g., "discovery")
        project: Project name for project-scoped execution (uses projects/<project>/)
        project_dir: Custom project directory containing agents/ folder
        output_dir: Custom directory to write output files
    """
    # Project-scoped execution
    if project:
        base_path = Path.cwd()
        project_path = base_path / "projects" / project
        
        # Verify project directory exists
        if not project_path.exists():
            print(f"❌ Error: Project directory not found: {project_path}")
            print(f"   Create it first: mkdir -p projects/{project}")
            return
        
        # Read project context
        context_file = project_path / "project-context.md"
        if not context_file.exists():
            print(f"❌ Error: Project context not found: {context_file}")
            print(f"   Create it first to declare your project scope and requirements.")
            return
        
        try:
            with open(context_file, "r") as f:
                project_context = f.read()
        except Exception as e:
            print(f"❌ Error reading project context: {e}")
            return
        
        # Set paths for project-scoped execution
        agent_prompt_path = base_path / "agents" / f"{agent}-agent.md"
        output_file = project_path / f"{agent}.md"
        
    # Custom path execution
    else:
        project_path = Path(project_dir).resolve()
        output_path = Path(output_dir).resolve()
        
        agent_prompt_path = project_path / "agents" / f"{agent}-agent.md"
        output_file = output_path / f"{agent}.md"
        project_context = None
    
    # Read agent prompt
    try:
        with open(agent_prompt_path, "r") as f:
            agent_prompt = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Agent definition not found at {agent_prompt_path}")
        return

    # Build full prompt
    if project_context:
        full_prompt = f"""# Project Context

{project_context}

---

# Agent Instructions

{agent_prompt}
"""
    else:
        full_prompt = agent_prompt

    print(f"🤖 Invoking {agent} agent...")
    if project:
        print(f"   Project: {project}")
    
    output = call_llm(full_prompt)

    print(f"🔍 Validating output...")
    validate_output(agent, output)

    with open(output_file, "w") as f:
        f.write(output)

    print(f"✅ {agent} completed successfully. Output saved to {output_file}")

