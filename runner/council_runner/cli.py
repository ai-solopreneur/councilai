import typer
from council_runner.runner import run_agent

app = typer.Typer()

@app.command()
def run(
    agent: str,
    project: str = typer.Option(None, help="Project name (uses projects/<project>/ directory)"),
    project_dir: str = typer.Option(None, help="Custom project directory containing agents/ folder"),
    output_dir: str = typer.Option(None, help="Custom directory to write output files")
):
    """
    Run a single CouncilAI agent.
    
    Use --project for project-scoped execution (recommended):
        council run discovery --project telehealth-bot
    
    Or use --project-dir and --output-dir for custom paths:
        council run discovery --project-dir /path/to/project --output-dir /path/to/output
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
    
    run_agent(agent, project=project, project_dir=project_dir, output_dir=output_dir)

if __name__ == "__main__":
    app()
