import pytest
import os
from council_runner.config import Config


def test_get_provider_default(monkeypatch):
    """Test default provider is openai"""
    monkeypatch.delenv("COUNCIL_LLM_PROVIDER", raising=False)
    assert Config.get_provider() == "openai"


def test_get_provider_from_env(monkeypatch):
    """Test provider from environment variable"""
    monkeypatch.setenv("COUNCIL_LLM_PROVIDER", "anthropic")
    assert Config.get_provider() == "anthropic"


def test_get_provider_invalid_raises_error(monkeypatch):
    """Test invalid provider raises ValueError"""
    monkeypatch.setenv("COUNCIL_LLM_PROVIDER", "invalid")
    
    with pytest.raises(ValueError, match="Invalid provider"):
        Config.get_provider()


def test_get_api_key_openai(monkeypatch):
    """Test getting OpenAI API key"""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
    
    key = Config.get_api_key("openai")
    assert key == "sk-test-key"


def test_get_api_key_anthropic(monkeypatch):
    """Test getting Anthropic API key"""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test-key")
    
    key = Config.get_api_key("anthropic")
    assert key == "sk-ant-test-key"


def test_get_api_key_missing_raises_error(monkeypatch):
    """Test missing API key raises ValueError"""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    
    with pytest.raises(ValueError, match="OPENAI_API_KEY environment variable not set"):
        Config.get_api_key("openai")


def test_get_model_defaults(monkeypatch):
    """Test model defaults"""
    monkeypatch.delenv("COUNCIL_OPENAI_MODEL", raising=False)
    monkeypatch.delenv("COUNCIL_ANTHROPIC_MODEL", raising=False)
    
    assert Config.get_model("openai") == "gpt-4"
    assert Config.get_model("anthropic") == "claude-3-5-sonnet-20241022"


def test_get_model_from_env(monkeypatch):
    """Test custom model from environment"""
    monkeypatch.setenv("COUNCIL_OPENAI_MODEL", "gpt-4-turbo")
    
    assert Config.get_model("openai") == "gpt-4-turbo"
