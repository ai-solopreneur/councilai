from council_runner.config import Config

def call_llm(prompt: str) -> str:
    """
    Call configured LLM provider with the given prompt.
    
    Supports OpenAI and Anthropic based on COUNCIL_LLM_PROVIDER env var.
    """
    provider = Config.get_provider()
    api_key = Config.get_api_key(provider)
    model = Config.get_model(provider)
    
    if provider == "openai":
        return _call_openai(prompt, api_key, model)
    elif provider == "anthropic":
        return _call_anthropic(prompt, api_key, model)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


def _call_openai(prompt: str, api_key: str, model: str) -> str:
    """Call OpenAI API"""
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("openai package not installed. Run: pip install openai")
    
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant following CouncilAI governance protocols."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    return response.choices[0].message.content


def _call_anthropic(prompt: str, api_key: str, model: str) -> str:
    """Call Anthropic API"""
    try:
        from anthropic import Anthropic
    except ImportError:
        raise ImportError("anthropic package not installed. Run: pip install anthropic")
    
    client = Anthropic(api_key=api_key)
    
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    return response.content[0].text
