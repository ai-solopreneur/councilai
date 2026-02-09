def validate_output(agent: str, output: str):
    if not output.strip():
        raise ValueError("Agent output is empty")
