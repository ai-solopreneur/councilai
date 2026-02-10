import pytest
from unittest.mock import Mock, patch, MagicMock
from council_runner.llm import call_llm


def test_call_llm_with_openai_provider(mocker):
    """Test LLM call with OpenAI provider"""
    # Mock config
    mocker.patch('council_runner.llm.Config.get_provider', return_value='openai')
    mocker.patch('council_runner.llm.Config.get_api_key', return_value='test-key')
    mocker.patch('council_runner.llm.Config.get_model', return_value='gpt-4')
    
    # Mock the _call_openai function
    mocker.patch('council_runner.llm._call_openai', return_value="Test response from OpenAI")
    
    result = call_llm("Test prompt")
    
    assert result == "Test response from OpenAI"


def test_call_llm_with_anthropic_provider(mocker):
    """Test LLM call with Anthropic provider"""
    # Mock config
    mocker.patch('council_runner.llm.Config.get_provider', return_value='anthropic')
    mocker.patch('council_runner.llm.Config.get_api_key', return_value='test-key')
    mocker.patch('council_runner.llm.Config.get_model', return_value='claude-3-5-sonnet-20241022')
    
    # Mock the _call_anthropic function
    mocker.patch('council_runner.llm._call_anthropic', return_value="Test response from Claude")
    
    result = call_llm("Test prompt")
    
    assert result == "Test response from Claude"


def test_call_llm_invalid_provider(mocker):
    """Test that invalid provider raises error"""
    mocker.patch('council_runner.llm.Config.get_provider', return_value='invalid')
    mocker.patch('council_runner.llm.Config.get_api_key', side_effect=ValueError("Unknown provider: invalid"))
    
    with pytest.raises(ValueError, match="Unknown provider"):
        call_llm("Test prompt")
