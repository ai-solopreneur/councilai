import typer
from council_runner.runner import run_agent

app = typer.Typer()

@app.command()
def run(
    agent: str,
    project_dir: str = typer.Option(".", help="Project directory containing agents/ folder"),
    output_dir: str = typer.Option(".", help="Directory to write output files")
):
    """
    Run a single CouncilAI agent.
    """
    run_agent(agent, project_dir, output_dir)

if __name__ == "__main__":
    app()
