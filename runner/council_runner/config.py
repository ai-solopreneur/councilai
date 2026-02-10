import os
from typing import Literal
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

LLMProvider = Literal["openai", "anthropic"]

class Config:
    """Configuration for CouncilAI Runner"""
    
    @staticmethod
    def get_provider() -> LLMProvider:
        """Get configured LLM provider"""
        provider = os.getenv("COUNCIL_LLM_PROVIDER", "openai").lower()
        if provider not in ["openai", "anthropic"]:
            raise ValueError(f"Invalid provider: {provider}. Must be 'openai' or 'anthropic'")
        return provider
    
    @staticmethod
    def get_api_key(provider: LLMProvider) -> str:
        """Get API key for specified provider"""
        if provider == "openai":
            key = os.getenv("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY environment variable not set")
            return key
        elif provider == "anthropic":
            key = os.getenv("ANTHROPIC_API_KEY")
            if not key:
                raise ValueError("ANTHROPIC_API_KEY environment variable not set")
            return key
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    @staticmethod
    def get_model(provider: LLMProvider) -> str:
        """Get model name for specified provider"""
        if provider == "openai":
            return os.getenv("COUNCIL_OPENAI_MODEL", "gpt-4")
        elif provider == "anthropic":
            return os.getenv("COUNCIL_ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        else:
            raise ValueError(f"Unknown provider: {provider}")
