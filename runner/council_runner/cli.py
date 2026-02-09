import typer
from council_runner.runner import run_agent

app = typer.Typer()

@app.command()
def run(agent: str):
    """
    Run a single CouncilAI agent.
    """
    run_agent(agent)

if __name__ == "__main__":
    app()
