import typer
from rich.console import Console
from council_runner.runner import run_agent, run_demo

console = Console()

BANNER = """
[bold cyan]
  _____                         _ _         _____ 
 / ____|                       (_) |   /\  |_   _|
| |     ___  _   _ _ __   ___ _ _| |  /  \   | |  
| |    / _ \| | | | '_ \ / __| | | | / /\ \  | |  
| |___| (_) | |_| | | | | (__| | | |/ ____ \_| |_ 
 \_____\___/ \__,_|_| |_|\___|_|_|_/_/    \_\_____|
[/bold cyan]
[dim]AI-Driven SDLC Governance Meta-System[/dim]
"""

app = typer.Typer(
    help="""
    CouncilAI Utility: A governance-first, multi-agent AI framework for the SDLC.
    
    This utility allows you to initialize projects and run specialized agents (Discovery, PRD, Architecture, etc.) 
    to build a robust, compliant, and audit-ready governance trail for your software.
    """,
    add_completion=False
)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        console.print(BANNER)
        console.print(ctx.get_help())

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
    Sequence: Discovery -> PRD -> Architecture -> Security -> Compliance -> Testing -> Release-Governance.
    """
    from council_runner.runner import run_all_agents
    run_all_agents(project)

@app.command()
def security(
    project: str = typer.Option(..., "--project", "-p", help="Project name to run security audit for")
):
    """
    Run the Security Agent for a specific project.
    Conducts STRIDE threat modeling and OWASP Top 10 for LLM mapping.
    """
    success = run_agent("security", project=project)
    if not success:
        raise typer.Exit(1)

@app.command()
def demo():
    """
    Run a one-click CouncilAI demo using the 'My Bottle' showcase.
    This will copy the showcase to 'demo-run/' and open the folder.
    """
    run_demo()

if __name__ == "__main__":
    app()
