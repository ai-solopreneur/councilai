import pytest
from council_runner.validation import validate_output


def test_validate_empty_output_raises_error():
    """Test that empty output raises ValueError"""
    with pytest.raises(ValueError, match="Agent output is empty"):
        validate_output("test", "")


def test_validate_whitespace_only_raises_error():
    """Test that whitespace-only output raises ValueError"""
    with pytest.raises(ValueError, match="Agent output is empty"):
        validate_output("test", "   \n\t  ")


def test_validate_valid_output_passes():
    """Test that valid output passes validation"""
    valid_output = """# Test Output
    
This is valid content.
"""
    # Should not raise any exception
    validate_output("test", valid_output)


def test_validate_minimal_output_passes():
    """Test that minimal but non-empty output passes"""
    validate_output("test", "x")
