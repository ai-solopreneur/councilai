import pytest
from pathlib import Path
from council_runner.runner import run_agent


def test_run_agent_with_project_flag(tmp_path, mocker, mock_llm_response):
    """Test project-scoped execution with --project flag"""
    # Create project structure
    project_dir = tmp_path / "projects" / "test-project"
    project_dir.mkdir(parents=True)
    
    # Create project-context.md
    context_file = project_dir / "project-context.md"
    context_file.write_text("# Test Project\n\nThis is a test project context.")
    
    # Create agents directory
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir()
    (agents_dir / "discovery-agent.md").write_text("# Discovery Agent\n\nRun discovery.")
    
    # Mock LLM
    mocker.patch('council_runner.runner.call_llm', return_value=mock_llm_response)
    
    # Change to tmp_path
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        
        # Run with --project flag
        run_agent("discovery", project="test-project")
        
        # Verify output file created in project directory
        output_file = project_dir / "discovery.md"
        assert output_file.exists()
        assert mock_llm_response in output_file.read_text()
    finally:
        os.chdir(original_cwd)


def test_run_agent_missing_project_directory(tmp_path, capsys):
    """Test error when project directory doesn't exist"""
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        
        run_agent("discovery", project="nonexistent-project")
        
        captured = capsys.readouterr()
        assert "❌ Error: Project directory not found" in captured.out
        assert "nonexistent-project" in captured.out
    finally:
        os.chdir(original_cwd)


def test_run_agent_missing_project_context(tmp_path, capsys):
    """Test error when project-context.md is missing"""
    # Create project directory but no project-context.md
    project_dir = tmp_path / "projects" / "test-project"
    project_dir.mkdir(parents=True)
    
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        
        run_agent("discovery", project="test-project")
        
        captured = capsys.readouterr()
        assert "❌ Error: Project context not found" in captured.out
        assert "project-context.md" in captured.out
    finally:
        os.chdir(original_cwd)


def test_project_context_injected_into_prompt(tmp_path, mocker, mock_llm_response):
    """Test that project context is injected into LLM prompt"""
    # Create project structure
    project_dir = tmp_path / "projects" / "test-project"
    project_dir.mkdir(parents=True)
    
    context_content = "# Test Project Context\n\nSpecial requirements here."
    (project_dir / "project-context.md").write_text(context_content)
    
    # Create agents directory
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir()
    (agents_dir / "discovery-agent.md").write_text("# Discovery Agent")
    
    # Mock LLM and capture the prompt
    mock_call_llm = mocker.patch('council_runner.runner.call_llm', return_value=mock_llm_response)
    
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        run_agent("discovery", project="test-project")
        
        # Verify LLM was called with context injected
        call_args = mock_call_llm.call_args[0][0]
        assert "# Project Context" in call_args
        assert context_content in call_args
        assert "# Agent Instructions" in call_args
    finally:
        os.chdir(original_cwd)
