from council_runner.llm import call_llm
from council_runner.validation import validate_output

def run_agent(agent: str):
    prompt_path = f"../agents/{agent}-agent.md"
    output_path = f"{agent}.md"

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

    with open(output_path, "w") as f:
        f.write(output)

    print(f"✅ {agent} completed successfully. Output saved to {output_path}")
