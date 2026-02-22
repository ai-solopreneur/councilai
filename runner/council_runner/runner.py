import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from council_runner.llm import call_llm
from council_runner.validation import validate_output

console = Console()

def run_agent(
    agent: str, 
    project: Optional[str] = None,
    project_dir: Optional[str] = None, 
    output_dir: Optional[str] = None
) -> bool:
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
            print(f"   Create it first: council init \"Your Idea\" --project {project}")
            return False
        
        # Read project context
        context_file = project_path / "project-context.md"
        if not context_file.exists():
            print(f"❌ Error: Project context not found: {context_file}")
            print(f"   Create it first to declare your project scope and requirements.")
            print(f"   Run: council init \"Your Idea\" --project {project}")
            return False
        
        try:
            with open(context_file, "r") as f:
                project_context = f.read()
        except Exception as e:
            print(f"❌ Error reading project context: {e}")
            return False
        
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
        return False

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

    console.print(f"[bold blue]🤖 Invoking {agent} agent...[/bold blue]")
    if project:
        console.print(f"   Project: {project}")
    
    output = call_llm(full_prompt)

    console.print(f"[yellow]🔍 Validating output...[/yellow]")
    validate_output(agent, output)

    with open(output_file, "w") as f:
        f.write(output)

    console.print(f"[green]✅ {agent} completed successfully.[/green] Output saved to [bold]{output_file}[/bold]")
    return True

def init_project(prompt: str, project: str) -> bool:
    """
    Initialize a new project by generating project-context.md from a prompt.
    """
    base_path = Path.cwd()
    project_path = base_path / "projects" / project
    agent_prompt_path = base_path / "agents" / "init-agent.md"
    output_file = project_path / "project-context.md"

    # Read init agent prompt
    try:
        with open(agent_prompt_path, "r") as f:
            agent_prompt = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Init agent definition not found at {agent_prompt_path}")
        return False

    # Create project directory
    project_path.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Initializing project: {project}...")
    full_prompt = f"""# User Intent

{prompt}

---

# Agent Instructions

{agent_prompt}"""

    output = call_llm(full_prompt)

    with open(output_file, "w") as f:
        f.write(output)

    print(f"✨ Project initialized. Context saved to {output_file}")
    print(f"👉 Next step: council discovery --project {project}")
    return True

def run_all_agents(project: str):
    """
    Run the full CouncilAI agent lifecycle for a project.
    """
    agents = ["discovery", "prd", "architecture", "compliance", "testing", "release-governance"]
    
    console.print(f"[bold magenta]🏁 Starting full CouncilAI lifecycle for project: {project}[/bold magenta]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        overall_task = progress.add_task("[cyan]Overall Progress", total=len(agents))
        
        for agent in agents:
            progress.update(overall_task, description=f"[bold green]Running {agent} agent...")
            success = run_agent(agent, project=project)
            if not success:
                console.print(f"[bold red]⛔ Lifecycle halted due to failure in {agent} agent.[/bold red]")
                return
            progress.advance(overall_task)

    console.print("=" * 40)
    console.print(f"[bold green]🎉 Full lifecycle complete for project: {project}[/bold green]")

def run_demo():
    """
    Run a demo by copying an existing showcase and opening it.
    """
    base_path = Path.cwd()
    demo_dest = base_path / "demo-run"
    showcase_src = base_path / "showcase" / "my-bottle"

    console.print("[bold yellow]🚀 Launching CouncilAI Demo...[/bold yellow]")
    
    if demo_dest.exists():
        shutil.rmtree(demo_dest)
    
    shutil.copytree(showcase_src, demo_dest)
    
    console.print(f"[green]✨ Demo project established in:[/green] [bold]{demo_dest}[/bold]")
    console.print("[blue]📂 Opening demo folder...[/blue]")

    # Cross-platform open
    try:
        project_to_open = demo_dest
        if sys.platform == "darwin":
            subprocess.run(["open", str(project_to_open)])
        elif sys.platform == "win32":
            os.startfile(project_to_open)
        else:
            subprocess.run(["xdg-open", str(project_to_open)])
    except Exception as e:
        console.print(f"[red]Could not open folder automatically: {e}[/red]")
    
    console.print("\n[bold green]Try running:[/bold green]")
    console.print(f"council all --project demo-run (if you have API keys set up)")

