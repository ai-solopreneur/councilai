import pytest
from pathlib import Path
from council_runner.runner import run_agent


def test_run_agent_with_custom_project_dir(temp_project_dir, temp_output_dir, mocker, mock_llm_response):
    """Test that runner uses custom project directory"""
    # Mock the LLM call
    mocker.patch('council_runner.runner.call_llm', return_value=mock_llm_response)
    
    # Run agent with custom directories
    run_agent("test", project_dir=temp_project_dir, output_dir=temp_output_dir)
    
    # Verify output file was created in correct location
    output_file = Path(temp_output_dir) / "test.md"
    assert output_file.exists()
    assert mock_llm_response in output_file.read_text()


def test_run_agent_missing_agent_file(temp_project_dir, temp_output_dir, capsys):
    """Test error handling when agent file doesn't exist"""
    run_agent("nonexistent", project_dir=temp_project_dir, output_dir=temp_output_dir)
    
    captured = capsys.readouterr()
    assert "❌ Error: Agent definition not found" in captured.out


def test_run_agent_default_paths(mocker, mock_llm_response, tmp_path):
    """Test that default paths work correctly"""
    # Create agents directory in tmp_path
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir()
    (agents_dir / "test-agent.md").write_text("# Test")
    
    # Mock LLM
    mocker.patch('council_runner.runner.call_llm', return_value=mock_llm_response)
    
    # Change to tmp_path and run with defaults
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        run_agent("test")
        
        # Verify output in current directory
        assert (tmp_path / "test.md").exists()
    finally:
        os.chdir(original_cwd)


def test_path_resolution_with_pathlib(temp_project_dir, temp_output_dir):
    """Test that Path objects are resolved correctly"""
    from pathlib import Path
    
    project_path = Path(temp_project_dir)
    output_path = Path(temp_output_dir)
    
    # Paths should resolve to absolute paths
    assert project_path.resolve().is_absolute()
    assert output_path.resolve().is_absolute()
