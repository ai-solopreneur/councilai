import typer
from council_runner.runner import run_agent

app = typer.Typer()

@app.command()
def run(
    agent: str,
    project: str = typer.Option(None, "--project", "-p", help="Project name (uses projects/<project>/ directory)"),
    project_dir: str = typer.Option(None, help="Custom project directory containing agents/ folder"),
    output_dir: str = typer.Option(None, help="Custom directory to write output files")
):
    """
    Run a single CouncilAI agent.
    
    Use --project for project-scoped execution (recommended):
        council run discovery --project telehealth-bot
    
    Or run all agents at once:
        council all --project telehealth-bot
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
    
    Example:
        council init "I want to build a bar bottle tracking app" --project my-bottle
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
    Run the full CouncilAI agent lifecycle (discovery -> prd -> architecture -> compliance -> testing -> release-governance).
    
    Example:
        council all --project my-bottle
    """
    from council_runner.runner import run_all_agents
    run_all_agents(project)

if __name__ == "__main__":
    app()
