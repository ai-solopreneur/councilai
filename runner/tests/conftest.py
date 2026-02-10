import pytest
from pathlib import Path
import tempfile
import shutil

@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory with agents/ folder"""
    temp_dir = tempfile.mkdtemp()
    agents_dir = Path(temp_dir) / "agents"
    agents_dir.mkdir()
    
    # Create a test agent file
    test_agent = agents_dir / "test-agent.md"
    test_agent.write_text("""# Test Agent

Generate a simple test output.
""")
    
    yield temp_dir
    
    # Cleanup
    shutil.rmtree(temp_dir)


@pytest.fixture
def temp_output_dir():
    """Create a temporary output directory"""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing"""
    return """# Test Output

This is a test output from the mocked LLM.

## Section 1
Content here.
"""
