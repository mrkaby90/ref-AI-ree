"""
Tests for image utilities
"""

import pytest
from pathlib import Path
from src.utils.image_utils import load_image


def test_load_image_nonexistent():
    """Test loading a non-existent image file"""
    result = load_image("nonexistent_image.jpg")
    assert result is None


# Note: Actual image processing tests require sample image files
# Add more tests when example images are available in examples/pictures/
