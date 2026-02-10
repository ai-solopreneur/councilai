import typer
from council_runner.runner import run_agent

app = typer.Typer(
    help="""
    CouncilAI Utility: A governance-first, multi-agent AI framework for the SDLC.
    
    This utility allows you to initialize projects and run specialized agents (Discovery, PRD, Architecture, etc.) 
    to build a robust, compliant, and audit-ready governance trail for your software.
    """,
    add_completion=False
)

@app.command()
def run(
    agent: str,
    project: str = typer.Option(None, "--project", "-p", help="Project name (uses projects/<project>/ directory)"),
    project_dir: str = typer.Option(None, help="Custom project directory containing agents/ folder"),
    output_dir: str = typer.Option(None, help="Custom directory to write output files")
):
    """
    Run a single CouncilAI agent.
    
    Examples:
    
    1. Run discovery for a named project (Recommended):
       $ council run discovery --project my-app
    
    2. Run PRD agent with a shortcut:
       $ council run prd -p my-app
    
    3. Run an agent with custom paths (Advanced):
       $ council run discovery --project-dir ./custom --output-dir ./results
    """
    # Validate mutually exclusive options
    if project and (project_dir or output_dir):
        print("❌ Error: --project cannot be used with --project-dir or --output-dir")
        raise typer.Exit(1)
    
    # Set defaults if no options provided
    if not project and not project_dir:
        project_dir = "."
    if not project and not output_dir:
        output_dir = "."
    
    success = run_agent(agent, project=project, project_dir=project_dir, output_dir=output_dir)
    if not success:
        raise typer.Exit(1)

@app.command()
def init(
    prompt: str = typer.Argument(..., help="Brief description of the project you want to build"),
    project: str = typer.Option(..., "--project", "-p", help="Project name (will create projects/<name>/)")
):
    """
    Initialize a new project context from a brief idea. 
    CouncilAI will expand your prompt into a full 'project-context.md' file.
    
    Examples:
    
    1. Simple initialization:
       $ council init "A marketplace for fresh vegetables" -p fresh-market
    
    2. Detailed initialization:
       $ council init "HIPAA-compliant telehealth app with AI triage" -p health-bot
    """
    from council_runner.runner import init_project
    success = init_project(prompt, project)
    if not success:
        raise typer.Exit(1)

@app.command(name="all")
def all_agents(
    project: str = typer.Option(..., "--project", "-p", help="Project name to run lifecycle for")
):
    """
    Run the full CouncilAI agent lifecycle in one shot.
    Sequence: Discovery -> PRD -> Architecture -> Compliance -> Testing -> Release-Governance.
    
    Examples:
    
    1. Run full lifecycle for my project:
       $ council all --project my-app
    
    2. Using the -p shortcut:
       $ council all -p my-app
    """
    from council_runner.runner import run_all_agents
    run_all_agents(project)

if __name__ == "__main__":
    app()
